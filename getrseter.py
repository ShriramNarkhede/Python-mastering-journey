class car:
 def get(self,color,style):
      self.color=color
      self.style=style
 def put(self):
      print(self.color)
      print(self.style)
c=car()
c.get('Brio','Red')
c.put()