import qrcode
url = input("Enter the URL to generate QR code: ")
file_path = 'C:\\Users\\pvire\\OneDrive\\qrcode.png'

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)