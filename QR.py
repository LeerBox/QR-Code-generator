# ASCII art
ascii_art = """


 .d88888b.  8888888b.        .d8888b.   .d88888b.  8888888b.  8888888888 
d88P" "Y88b 888   Y88b      d88P  Y88b d88P" "Y88b 888  "Y88b 888        
888     888 888    888      888    888 888     888 888    888 888        
888     888 888   d88P      888        888     888 888    888 8888888    
888     888 8888888P"       888        888     888 888    888 888        
888 Y8b 888 888 T88b        888    888 888     888 888    888 888        
Y88b.Y8b88P 888  T88b       Y88b  d88P Y88b. .d88P 888  .d88P 888        
 "Y888888"  888   T88b       "Y8888P"   "Y88888P"  8888888P"  8888888888 
       Y8b                                                               
                                                                         
                                                                                                                                     
"""

import qrcode
import os
from PIL import Image
import re

# Function to generate a QR code and save it in the "QR CODES" directory
def generate_qr_code_and_save(data):
    # Create the "QR CODES" directory if it doesn't exist
    output_dir = "QR CODES"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine the data type (URL, phone number, or app account)
    if re.match(r'https?://', data):
        data_type = 'URL'
    elif re.match(r'\+?\d{10,}', data):
        data_type = 'Phone Number'
    else:
        data_type = 'App Account'

    # Generate a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Find the next available numerical filename
    filename = 0
    while True:
        file_path = os.path.join(output_dir, f"{filename:04d}_{data_type}.png")
        if not os.path.exists(file_path):
            break
        filename += 1

    # Save the QR code image in the "QR CODES" directory
    qr_img.save(file_path)
    print(f"QR code for {data_type} saved as {file_path}")

def main():
    try:
        data = input("Enter URL, Phone Number, or App Account to convert to QR code: ")
        generate_qr_code_and_save(data)
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")

if __name__ == "__main__":
    print(ascii_art)
    main()
