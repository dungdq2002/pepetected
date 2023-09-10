from PIL import Image, ImageDraw, ImageFont

class GenerateImageByText:
    @staticmethod
    def gen(text: str) -> Image:
        # Create a blank image with a white background
        width, height = 400, 200
        background_color = (255, 255, 255)  # White
        image = Image.new("RGB", (width, height), background_color)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Define the text and font
        text = "Hello, PNG!"
        font_color = (0, 0, 0)  # Black

        font_size = 16
        font_path = "sample/font/UbuntuMono-Regular.ttf"  # Replace with the path to a TrueType font file

        font = ImageFont.truetype(font_path, font_size)

        # Calculate text size and position
        # text_width, text_height = draw.textsize(text)
        # x = (width - text_width) / 2
        # y = (height - text_height) / 2

        # Draw the text on the image
        draw.text((50, 50), text, fill = font_color, font = font)

        return image
