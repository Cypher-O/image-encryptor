from PIL import Image

class ImageProcessor:
    @staticmethod
    def process_image(input_path, output_path, operation):
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                if operation == "encrypt":
                    processed_pixel = (b, g, r)  # Swap red and blue channels
                elif operation == "decrypt":
                    processed_pixel = (b, g, r)  # Swap red and blue channels back
                else:
                    raise ValueError("Invalid operation. Use 'encrypt' or 'decrypt'.")
                pixels[i, j] = processed_pixel

        img.save(output_path)
        return f"Image {operation}ed successfully!"

    @staticmethod
    def encrypt_image(input_path, output_path):
        return ImageProcessor.process_image(input_path, output_path, "encrypt")

    @staticmethod
    def decrypt_image(input_path, output_path):
        return ImageProcessor.process_image(input_path, output_path, "decrypt")