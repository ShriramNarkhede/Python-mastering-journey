from html.parser import HTMLParser
import requests as r
data = r.get("https://www.geeksforgeeks.org/introduction-to-tensorflow/")
class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data

f = HTMLFilter()
f.feed(data.text)
print(f.text)