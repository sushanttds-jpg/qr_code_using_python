print("========= Simple code to generate qr code =========")
import qrcode
Taking_input = input("Enter anything you want to convert it to qr code:")
image_generated =qrcode.make(Taking_input)
image_generated.save('image.png')
print("Your Qr code is generated successfully")