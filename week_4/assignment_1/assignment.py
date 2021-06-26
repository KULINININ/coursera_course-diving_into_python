from tempfile import gettempdir
from os.path import join, exists
from uuid import uuid4


class File:
    def __init__(self, path):
        self.path = path
        self.current = 0

        if not exists(path):
            with open(path, 'w') as file:
                pass
        
    def read(self):
        with open(self.path, 'r') as file:
            return file.read()
        
    def write(self, string):
        with open(self.path, 'w') as file:
            file.write(string)
    
    def __add__(self, other):
        obj = File(join(gettempdir(), uuid4().hex))
        obj.write(self.read() + other.read())
        return obj
    
    def __str__(self):
        return self.path
    
    def __iter__(self):
        return self
    
    def __next__(self):
        with open(self.path, 'r') as file:
            file.seek(self.current)
            
            line = file.readline()
            if not line:
                self.current = 0
                raise StopIteration('EOF')
                
            self.current = file.tell()
            
            return line
