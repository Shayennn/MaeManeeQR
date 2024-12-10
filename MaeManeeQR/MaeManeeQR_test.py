from MaeManeeQR import MaeManeeQR
import pytest
from PyCRC.CRCCCITT import CRCCCITT


def test_crc16():
    crc_obj = CRCCCITT("FFFF")
    crc = crc_obj.calculate(
        "00020101021129370016A000000677010111011300660000000005802TH53037646304"
    )

    # Expected CRC16 checksum 0x8956
    assert crc == 0x8956, "CRC16 checksum should be 0x8956."


def test_maemaneeqr():
    mmn = MaeManeeQR.MaeManeeQR("014000000820910", "TESTPYTHON")
    mmn.setAmount(14.53)
    mmn_str = str(mmn)

    print(mmn_str)

    assert mmn_str, "MaeManeeQR string representation should not be empty."

    # Expected 0215014000000820910 in mmn_str
    assert "0215014000000820910" in mmn_str, "ShopID representation is incorrect."

    # Expected 0310TESTPYTHON in mmn_str
    assert "0310TESTPYTHON" in mmn_str, "ShopName representation is incorrect."

    # Expected 540514.53 in mmn_str
    assert "540514.53" in mmn_str, "Amount representation is incorrect."

    # Expected data (without 8 last characters) in mmn_str
    assert (
        mmn_str[:-8]
        == "00020101021230720016A000000677010112011501075360001028602150140000008209100310TESTPYTHON5303764540514.535802TH622007160000000000085234"
    ), "Data representation is incorrect."

    crc_obj = CRCCCITT("FFFF")
    crc = crc_obj.calculate(mmn_str[:-4])
    crc_hex = format(crc, "X").upper()

    # Expected CRC16 checksum 0x75F0 in mmn_str
    assert crc_hex in mmn_str, "CRC16 checksum representation is incorrect."


if __name__ == "__main__":
    pytest.main()
