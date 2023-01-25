from transbank import oneclick as BaseOneClick
from transbank.common.integration_type import IntegrationType
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.webpay.webpay_plus import WebpayPlus


tx = Transaction(WebpayOptions("597055555532".WEBPAY_PLUS, "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C".WEBPAY, IntegrationType.TEST))
response = tx.create(buy_order="123456", amount=10000, return_url="http://127.0.0.1:8000/venta/carrito/")
Transaction.create(tx)