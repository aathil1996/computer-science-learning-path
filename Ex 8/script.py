from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap():
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for number in range(size)]
    
  def hash(self, key):
    return sum(key.encode())
    
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
      if key == i[0]:
        i[1] = value
      else:
        list_at_array.insert(payload)
      
    
    
  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] is key:
        return item[1]
      else:
        return None
    

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
  
print(blossom.retrieve('daisy'))
    
    
  