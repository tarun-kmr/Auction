from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from Auction.celery import app


REPORT_TEMPLATE = """
Congratulations!!!

{% for auction in auctions %}
        "Item :: {{ auction.name }}"
{% endfor %}
"""


@app.task
def send_email():
    from api.models import AuctionItem
    for user in get_user_model().objects.all():
        auctions = AuctionItem.objects.filter(winner=user)
        if not auctions:
            continue

        template = Template(REPORT_TEMPLATE)
        send_mail(
            'Congrats',
            template.render(context=Context({'auctions': auctions})),
            'tarun.kumar@fulfil.io',
            [user.email],
            fail_silently=False,
        )
