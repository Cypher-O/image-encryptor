from src import ImageProcessor

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = ImageProcessor()

        self.view.encrypt_signal.connect(self.encrypt_image)
        self.view.decrypt_signal.connect(self.decrypt_image)

    def encrypt_image(self, input_path, output_path):
        try:
            result = self.model.encrypt_image(input_path, output_path)
            self.view.show_success(result)
        except Exception as e:
            self.view.show_error(f"Error during encryption: {str(e)}")

    def decrypt_image(self, input_path, output_path):
        try:
            result = self.model.decrypt_image(input_path, output_path)
            self.view.show_success(result)
        except Exception as e:
            self.view.show_error(f"Error during decryption: {str(e)}")