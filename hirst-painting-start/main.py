import colorgram
import random

rgb_color = []
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 35)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r, g, b)
    rgb_color.append(rgb_tuple)
    
# print(rgb_color)