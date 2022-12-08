from pprint import pprint

input = open('input.txt', 'r').read().strip().split('\n\n')

algo = input[0]

input_image = []

for line in input[1].split('\n'):
    input_image.append(line)


def pixels_to_decimal(pixels):
    binary_string = ''
    for pixel in pixels:
        if pixel == '#':
            binary_string += '1'
        else:
            binary_string += '0'
    return int(binary_string, 2)


output_image = []


def enhance(image, step):
    output_image = []
    for y in range(-1, len(image)+1):
        output_image.append([])
        for x in range(-1, len(image[0])+1):
            square = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y),
                      (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
            pixels = ''
            for cell in square:
                pixel_in_infinity = '.' if step % 2 == 0 else '#'
                if cell[1] >= len(image) or cell[0] >= len(image[0]) or cell[0] < 0 or cell[1] < 0:
                    pixels += pixel_in_infinity
                else:
                    pixels += image[cell[1]][cell[0]]
            # print(pixels)
            decimal_repr = pixels_to_decimal(pixels)
            # print(decimal_repr)
            output_image[y+1].append(algo[decimal_repr])
    return output_image


def calculate_lit_pixels(image):
    counter = 0
    for line in image:
        for pixel in line:
            if pixel == '#':
                counter += 1
    return counter


output_image_file = open('output_image.txt', 'w')
for i in range(0, 50):
    print(i)
    input_image = enhance(input_image, i)

# for line in input_image:
#     output_image_file.write(''.join(line))
#     output_image_file.write('\n')
# print(input_image)
result = calculate_lit_pixels(input_image)
print("Result: {}".format(result))
