import png 

def encode(msg_path="inputs\\input_message.txt", img_path="inputs\\input_image.png"): 

    # read image 
    read_image = png.Reader(filename=img_path).asDirect()
    pixels = [list(row) for row in read_image[2]]

    if read_image[3]['alpha']: 
        for i in range(len(pixels)): 
            del pixels[i][3::4]

    width = read_image[3]['size'][0] 
    height = read_image[3]['size'][1] 

    # output image 
    write_image = png.Writer(width, height, greyscale=False) 
    write_image.write(open("outputs\\output_image.png", "wb"), pixels) 

encode() 