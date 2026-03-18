import qrcode as qr

img = qr.make("https://www.sarkariresult.com/")
img.save("sarkariresult.png")   
if img:
    print("QR code generated successfully!")
else:
    print("Failed to generate QR code.")