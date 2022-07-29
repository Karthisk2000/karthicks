class tamil:
    def project(self):
        print('avs college of arts and science:')

class surya(tamil):
    def project(self):
        #super().project()
        print('sri vidya mandir arts and science college:')

class karthick(surya):
    def project(self):
        #super().project()
        print('karpagam acamemy of higher eucation:')

obj = karthick()

obj.project()

