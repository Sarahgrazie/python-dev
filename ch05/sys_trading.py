from collections.abc import Callable, Iterable, Mapping
import threading
from typing import any 

class SysTrading(threading, Thread):
    def __init__(self: super, corp_nm, close, vol):
    #def__init__(self, corp_nm, close, vol):
        super.__init__()
        self.corp_nm = corp_nm
        self.close = close
        self.vol = vol
        
    def run(self):       # while 문에 들어가야 한다 원래는
        self.result = self.close *self.vol
        
        
    def getResult(self):
        return self.corp_nm + str(self.result)
    
    sam = SysTrading('삼성전자', 71400, 100)
    lg = SysTrading('LG전자', 104000, 100)
    
    sam.start()
    lg.start()
    
    print(sam.getResult())
    print(lg.getResult())