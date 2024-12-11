from ThaiPaymentQR import MaeManeeQR

mmn = MaeManeeQR("014000000820910", "Supatipanno")
mmn.setAmount(168.88)

print(str(mmn), end="")
