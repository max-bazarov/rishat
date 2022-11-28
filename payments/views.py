import os

import dotenv
from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer
from .services import PaymentSessionService

dotenv.load_dotenv()


class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class ItemDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payments/item_card.html'

    def get(self, request, pk) -> type[Response]:
        stripe_public_key = os.getenv('STRIPE_PUB_KEY')
        item = Item.objects.get(id=pk)
        return Response({'item': item, 'stripe_public_key': stripe_public_key})


class StripeSession(APIView):
    def get(self, request, pk) -> type[Response]:
        session_id = PaymentSessionService().create_session(item_id=pk)
        return Response({'session_id': session_id})


class CancelView(TemplateView):
    template_name = 'stripe/cancel.html'


class SuccessView(TemplateView):
    template_name = 'stripe/success.html'
