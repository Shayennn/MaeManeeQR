from .PromptPayField import PromptPayField
from .PromptPayQR import PromptPayQR


class MaeManeeQR(PromptPayQR):
    def __init__(self, shopID, Ref):
        super().__init__()
        bill_info_data = [
            PromptPayField('00', 'AppID', 'A000000677010112'),
            PromptPayField('01', 'BillerID', '010753600010286'),
            PromptPayField('02', 'ShopID', shopID),
            PromptPayField('03', 'Ref', Ref)
        ]
        self.additionalField = []
        bill_info = PromptPayField('30', 'billinfo', bill_info_data)
        unknow_scb = PromptPayField('07', 'unk', '0000000000085234')
        scb_add = PromptPayField('62', 'scbadd', [unknow_scb])
        self.fields['30'] = bill_info
        self.fields['62'] = scb_add
