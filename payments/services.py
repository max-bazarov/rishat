import os

import dotenv
import stripe

from .models import Item

dotenv.load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class PaymentSessionService:

    def create_session(self, item_id: int) -> int:
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price * 100),

                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url='http://localhost:8000/api/success',
            cancel_url='http://localhost:8000/api/cancel',
        )

        return session.id
