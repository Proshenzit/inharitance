class Phone:
  def call(self):
      print("You can call")

  def message(self):
      print("You can message")


class Samsung(Phone):
  def photo(self):
      print("You can take photo")


p = Phone()
s = Samsung()
p.call()
p.message()
s.photo()
print(issubclass(Samsung,Phone))




  
