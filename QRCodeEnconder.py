import qrcode
from PIL import Image

# Get the URL from the user
url = input("Enter the URL: ")

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # QR code version
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each QR code box
    border=4,  # Border size
)

# Add the URL to the QR code
qr.add_data(url)
qr.make(fit=True)

# Generate the QR code as an image
img = qr.make_image(fill_color="black", back_color="white")

# Display the QR code image
img.show()

# Save the QR code image to a file (optional)
img.save("my_qr_code.png")

print("QR code generated and displayed.")
