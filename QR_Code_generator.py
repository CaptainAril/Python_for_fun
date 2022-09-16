# Imoort QRCode from pyqrcode
import pyqrcode
import png

# String which represents the QR code
url = "https://www.clcoding.com/p/python.html"

# Generate QR code
url_QR = pyqrcode.create(url)
# Download and save the QR code to specific path
url_QR.png('C:\\Users\obeem\Documents\Programming\MacroTutor\MyQRCode.png', scale = 10)

#clcoding.com
