class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string: str) -> int:
        if not isinstance(string, str):
            raise TypeError('Must be a string')
        return sum(ord(x) for x in string)

    def add(self, key, value):
        hash_key = self.hash(key)
        print(hash_key)
        if hash_key not in self.collection:            
            self.collection[hash_key] = {key: value}            
        else:
            self.collection[hash_key][key] = value

    def remove(self, key) -> None:
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:            
            del self.collection[hash_key][key]
        else:
            return
    def lookup(self, key) -> bool|None:
        hash_key = self.hash(key)
        return self.collection[hash_key][key] if hash_key in self.collection and key in self.collection[hash_key] else None

teste = HashTable()
teste.add('golf', 'sport')
print(teste.collection)   
print(teste.lookup('golf')) 
teste.add('fcc','teste12')

print(teste.remove(''))