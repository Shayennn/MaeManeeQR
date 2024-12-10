from MaeManeeQR import MaeManeeQR
import pytest
from PyCRC.CRCCCITT import CRCCCITT


def constant_and_checksum_test(mmn_str: str):
    # Expected 000201 in mmn_str
    assert "000201" in mmn_str, "Prefix representation is incorrect."

    # Expected 010212 in mmn_str
    assert "010212" in mmn_str, "Payload Format Indicator representation is incorrect."

    # Expected 0016A000000677010112 in mmn_str
    assert (
        "0016A000000677010112" in mmn_str
    ), "Merchant Account Information representation is incorrect."

    # Expected 0115010753600010286 in mmn_str
    assert "0115010753600010286" in mmn_str, "Merchant Category Code representation is incorrect."

    # Expected 622007160000000000085234 in mmn_str
    assert (
        "622007160000000000085234" in mmn_str
    ), "Merchant Information representation is incorrect."

    # Expected 5303764 in mmn_str
    assert "5303764" in mmn_str, "Transaction Currency representation is incorrect."

    # Expected 5802TH in mmn_str
    assert "5802TH" in mmn_str, "Country Code representation is incorrect."

    crc_obj = CRCCCITT("FFFF")
    crc = crc_obj.calculate(mmn_str[:-4])
    crc_hex = format(crc, "X").upper()

    # Expected CRC16 checksum in mmn_str
    assert crc_hex in mmn_str, "CRC16 checksum representation is incorrect."


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

    assert mmn_str, "MaeManeeQR string representation should not be empty."

    constant_and_checksum_test(mmn_str)

    # Expected 0215014000000820910 in mmn_str
    assert "0215014000000820910" in mmn_str, "ShopID representation is incorrect."

    # Expected 0310TESTPYTHON in mmn_str
    assert "0310TESTPYTHON" in mmn_str, "ShopName representation is incorrect."

    # Expected 540514.53 in mmn_str
    assert "540514.53" in mmn_str, "Amount representation is incorrect."

    # Expected data (without 8 last characters) in mmn_str
    assert len(mmn_str[:-8]) == len(
        "00020101021230720016A000000677010112011501075360001028602150140000008209100310TESTPYTHON5303764540514.535802TH622007160000000000085234"
    ), "Data length is incorrect."


def test_maemaneeqr_2():
    mmn = MaeManeeQR.MaeManeeQR("014000000820910", "312121")
    mmn.setAmount(1212.00)
    mmn_str = str(mmn)

    assert mmn_str, "MaeManeeQR string representation should not be empty."

    constant_and_checksum_test(mmn_str)

    # Expected 0215014000000820910 in mmn_str
    assert "0215014000000820910" in mmn_str, "ShopID representation is incorrect."

    # Expected 0306312121 in mmn_str
    assert "0306312121" in mmn_str, "ShopName representation is incorrect."

    # Expected 54071212.00 in mmn_str
    assert "54071212.00" in mmn_str, "Amount representation is incorrect."

    # Expected data (without 8 last characters) in mmn_str
    assert len(mmn_str[:-8]) == len(
        "00020101021230680016A000000677010112011501075360001028602150140000008209100306312121530376454071212.005802TH622007160000000000085234"
    ), "Data length is incorrect."


if __name__ == "__main__":
    pytest.main()
