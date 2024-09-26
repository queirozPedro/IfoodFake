from rest_framework.serializers import ModelSerializer
from pedidos.models import Pedido
from pedidos.models import Item


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"


class ItemPedidoSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'nome', "preco"]

class PedidosCreateSerializer(ModelSerializer):

    class Meta:
        model = Pedido
        fields = ['cliente', 'endereco', 'item']


class PedidosSerializer(ModelSerializer):

    item = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['cliente', 'endereco', 'item', 'valor_total']


class PagamentoSerializer(ModelSerializer):

    class Meta:
        model = Pedido
        fields  = ['id', 'cliente', 'endereco', 'valor_total', 'pago']


    
