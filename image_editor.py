#!/usr/bin/python

image = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
new_list = [[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]]

# Division into color channels
#
# Done by LamMandy

def divide_channels(image):
    result = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(len(image[0][0])):
                pass
    for x in image:
        for y in x:
            for z in y:
                result.append([[z]])
            # for z in y:
            #     [list(z)]
                # for i in range(len(y)):
                    # n_lst.append(z)
                    # new_list[x][y][i] = z
                    # print(new_list[x][y][i])
    return result

def merge_channels(image: list) -> list:
    '''Function gets a list of the length channels of the 2-dimensional images composed of single colour channels, and unites then to a colourful image with the dimensions: rows X coloumns X channels'''
    pass

# Transition into grayscale
#
# Done by ITKozak

def from_rgb_to_gray(colored_image):
    pass

# Blurring
#
# Done by

def blur(size):
    pass

def add_kernel(image, kernel):
    pass

# Resize
#
# Done by

def bilinear_interpolation(image, x, y):
    pass

def resize(image, new_height, new_width):
    pass

# 90 Degree rotation
#
# Done by

def rotate(image, direction):
    pass

# Edge line recognition
#
# Done by

def extract_edges(image, blur_size, block_size, c):
    pass

# Reduction of colours in the image
# 
# Done by

def quantization(image, N):
    pass

def colored_img_quantizer(image, N):
    pass

# Adding images using mask
#
# Done by

def mask_generator(image1, image2, mask):
    pass

# Cartoonify
#
# Done by

def main_editor(image, blur_size, th_block_size, th_c, wuant_num_shades):
    pass

# Main function 

def main():
    # new = divide_channels(image)
    # print(new)
    # print(new_list)
    image_1 = [[[1, 2]]]
    print(divide_channels(image_1))

if __name__ == '__main__':
    main()