from PIL import Image, ImageDraw

# Read txt file
with open('DS0.txt') as f:
    lines = f.readlines()

coordinates = []

for line in lines:
    # Delete '\n' symbol from every dot and split by space
    formatted_line = line[:-1].split(' ')
    # Create single coordinate as tuple
    single_coordinate = (int(formatted_line[0]), int(formatted_line[1]))
    coordinates.append(single_coordinate)

# Create new image
out = Image.new("RGB", (540, 960), (255, 255, 255))
draw = ImageDraw.Draw(out)
# Fill canvas with prepared coordinates
draw.point(coordinates, fill='red')
# Show picture
out.show()
# Save picture
out.save("output.jpg")
