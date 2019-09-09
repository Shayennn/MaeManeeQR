class PromptPayField:
    code = None
    name = None
    value = []

    def __init__(self, code, name, value):
        self.code = code
        self.name = name
        self.value = value

    def __str__(self):
        outStr = str(int(self.code)).zfill(2)
        outData = ''
        if type(self.value) == str:
            outData = self.value
        else:
            for i in self.value:
                outData += str(i)
        outStr += str(len(outData)).zfill(2)
        outStr += outData
        return outStr
