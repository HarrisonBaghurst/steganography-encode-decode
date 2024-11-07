import png 

def encode(msg_path="inputs\\input_message.txt", img_path="inputs\\input_image.png"): 

    ### ---------- read text file ---------- ###
    text_file = open(msg_path, 'r') 
    text = text_file.readline() 
    msg_binary = '' 
    for char in text: 

        # convert char to binary code in exact 8 bit format
        binary = bin(ord(char))[2:]
        while len(binary) < 8: 
            binary = '0' + binary
        
        # add char binary to msg_binary 
        msg_binary += binary     

    ### ---------- read image ---------- ###
    read_image = png.Reader(filename=img_path).asDirect()
    pixels = [list(row) for row in read_image[2]]

    # if input image has alpha layer remove alpha layer 
    if read_image[3]['alpha']: 
        for i in range(len(pixels)): 
            del pixels[i][3::4]

    # get width and height of input image 
    width = read_image[3]['size'][0] 
    height = read_image[3]['size'][1] 

    ### ---------- encode binary into image ---------- ### 
    pixels_row = 0 
    pixels_column = 0 
    for i in range(len(msg_binary)): 
        if msg_binary[i] == '1': 
            if pixels[pixels_row][pixels_column] % 2 == 0: 
                pixels[pixels_row][pixels_column] += 1 
                if pixels[pixels_row][pixels_column] >= 256: 
                    pixels[pixels_row][pixels_column] -= 2
        else: 
            if pixels[pixels_row][pixels_column] % 2 != 0: 
                pixels[pixels_row][pixels_column] -= 1 
                if pixels[pixels_row][pixels_column] < 0: 
                    pixels[pixels_row][pixels_column] += 2
        pixels_column += 1
        if pixels_column >= len(pixels[0]): 
            pixels_column = 0 
            pixels_row += 1

    # add extra 8 bits to show end of message 
    for i in range(8): 
        if pixels[pixels_row][pixels_column] % 2 != 0: 
            pixels[pixels_row][pixels_column] -= 1 
        pixels_column += 1
        if pixels_column >= len(pixels[0]): 
            pixels_column = 0 
            pixels_row += 1

    ### ---------- output image ---------- ###
    write_image = png.Writer(width, height, greyscale=False, bitdepth=read_image[3]['bitdepth']) 
    write_image.write(open("outputs\\output_image.png", "wb"), pixels) 

encode() 