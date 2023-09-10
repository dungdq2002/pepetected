from PIL import Image

from stegatool.utils.genimg import GenerateImageByText

class Encoder:
    def encode_image(self, path_image: str, message: str, path_output: str) -> None:
        input_image = self.__read_image(path_image)
        modified_image = self.__encode(input_image, message)
        modified_image.save(path_output)
        
    def encode_text(self, cover_text: str, message: str, path_output: str) -> None:
        input_image = GenerateImageByText.gen(cover_text)
        modified_image = self.__encode(input_image, message)
        modified_image.save(path_output)


    def __encode(self, image: Image, message: str) -> Image:
        image = image.convert("RGBA")
        modified_image = image.copy()

        input_exec_bits = self.__str_to_bits(message)
        width, height = image.size
        index = 0
        for x in range(0, width):
            for y in range(0, height):
                if index < len(input_exec_bits):
                    pixel = list(image.getpixel((x, y)))
                    pixel[0] = self.__set_lsb(pixel[0], int(input_exec_bits[index]))
                    modified_image.putpixel((x, y), tuple(pixel))
                    index += 1
        return modified_image

    @staticmethod
    def __read_image(path_image: str) -> Image:
        try:
            return Image.open(path_image)
        except FileNotFoundError:
            print(f"File not found: {path_image}")
        except:
            print(f"Error reading image file {path_image}")

    @staticmethod
    def __str_to_bits(str: str) -> str:
        bits = ""
        for char in str:
            bits += bin(ord(char))[2:].zfill(8)
        bits += "00000000"
        return bits

    @staticmethod
    def __set_lsb(byte: int, bit: int) -> int:
        return byte & 0xfe | bit
