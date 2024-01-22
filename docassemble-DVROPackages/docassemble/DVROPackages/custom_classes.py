from docassemble.base.core import DAObject

class FirearmItem(DAObject):
    def init(self, *pargs, **kwargs):
        super(FirearmItem, self).init(*pargs, **kwargs)
        self.name = ""
        self.number = ""
        self.amount = ""
        self.location = ""

class AmmunitionItem(DAObject):
    def init(self, *pargs, **kwargs):
        super(AmmunitionItem, self).init(*pargs, **kwargs)
        self.name = ""
        self.amount = ""
        self.location = ""
