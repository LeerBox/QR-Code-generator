import qrcode
import os

def generate_filename(base_dir="."):
    """
    Generate a filename in ascending numerical order.

    Parameters:
    - base_dir (str): The directory to check for existing files. Default is the current directory.

    Returns:
    - str: A filename in the format "qr_code_X.png", where X is an ascending number.
    """
    counter = 1
    while True:
        filename = os.path.join(base_dir, f"qr_code_{counter}.png")
        if not os.path.exists(filename):
            return filename
        counter += 1

def url_to_qr(url):
    """
    Convert a URL (or any string) to a QR code and save it as an image file with an ascending numerical filename.

    Parameters:
    - url (str): The URL (or any string) to be converted to a QR code.

    Returns:
    None
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    output_file = generate_filename()
    
    img.save(output_file)
    print(f"QR code saved as {output_file}")

if __name__ == "__main__":
    input_string = input("Enter the URL or any string: ")
    url_to_qr(input_string)
