####################################
# Code to create a transaction
####################################

class TransactionMetadata():
    def __init__(self):
        self.hash : str = None
        self.ver : int = None
        self.vin_sz : int = None
        self.vout_sz : int = None
        self.lock_time : int = None
        self.size : int = None
        self.input : TransactionInput = None
        self.output : TransactionOutput = None

class TransactionInput():
    def __init__(self):
        self.hash : str = None
