from ThaiPaymentQR import KShopQR

mmn = KShopQR("EXT01000174879", "Supatipanno")
mmn.setAmount(168.88)

print(str(mmn), end="")
