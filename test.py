import qrcode
from MaeManeeQR import MaeManeeQR

mmn = MaeManeeQR.MaeManeeQR('014000000820910','TESTPYTHON')
mmn.setAmount(14.53)

qrcode.make(str(mmn), error_correction=qrcode.constants.ERROR_CORRECT_H).show()
