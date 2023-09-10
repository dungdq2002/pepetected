from PIL import Image

class Decoder:
    def decode(self, image_path: str) -> str:
        image = Image.open(image_path)
        image = image.convert("RGB")
        width, height = image.size
        bits = ""
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(image.getpixel((x, y)))
                bits += str(pixel[0] & 1)
        message = self.__bits_to_str(bits)
        return message
        
    @staticmethod
    def __bits_to_str(bits: str) -> str:
        res = ""
        for i in range(0, len(bits), 8):
            val = int(bits[i:i+8], 2)
            if val == 0: break
            res += chr(val)
        return res