import pygame

# Create a class for teh sprite sheet to make it reusable
class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        # You can use blit to display the image onto the square that appeared as blit works on surfaces, and image counts as one
        # the last perameter tells pygame that we want the image from coordinate 0,0 of the image, until the given width and height
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))

        # Makes the sprite bigger than it was originally with the given multiple
        image = pygame.transform.scale(image, (width * scale, height * scale))

        # Gets rid of the black background and makes it transparent
        image.set_colorkey(colour)
        return image