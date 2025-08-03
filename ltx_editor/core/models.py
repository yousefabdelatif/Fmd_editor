class LtxModel:
    def __init__(self):
        self.data = {}
    
    def get_data(self):
        return self.data
    
    def set_data(self, key, value):
        self.data[key] = value
