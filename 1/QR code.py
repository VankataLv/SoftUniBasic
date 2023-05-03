import pyqrcode


address = "https://dir.bg/"
url = pyqrcode.create(address)
url.png('test.png', scale=8)
