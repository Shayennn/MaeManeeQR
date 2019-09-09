# MaeManeeQR

A tool for generating SCB MaeManee QR Code.

## Requirement

* Python3
* [PyCRC](https://pypi.org/project/PyCRC/)

## Usage

``` python
from MaeManeeQR import MaeManeeQR


shopID = '014000000820910'  # Your ShopID from MaeManee App.
ref = 'ShayennnTestQR'  # Your message to include in the transaction when the payer has paid.

mmn = MaeManeeQR.MaeManeeQR(shopID, ref)
mmn.setAmount(14.53) # Amount to create QRCode

print(mmn)  # The QRCode content.

```

## License

[The MIT License.](LICENSE)
