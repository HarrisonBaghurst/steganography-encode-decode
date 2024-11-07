import png

def decode(img_path="inputs\\input_image.png"): 

    ### ---------- read image ---------- ###
    read_image = png.Reader(filename=img_path).asDirect()
    pixels = [list(row) for row in read_image[2]]

    ### ---------- read binary from image ---------- ### 
    previous_char = '' 
    pixels_row = 0 
    pixels_column = 0 
    chars = []
    while previous_char != '00000000': 
        previous_char = ''
        for i in range(8): 
            if pixels[pixels_row][pixels_column] % 2 == 0: 
                previous_char += '0'
            else: 
                previous_char += '1'
            pixels_column += 1 
            if pixels_column >= len(pixels[0]): 
                pixels_column = 0 
                pixels_row += 1
        if previous_char != '00000000': 
            chars.append(previous_char) 
    
    ### ---------- turn into readable text string ---------- ###
    output_string = '' 
    for char_bin in chars: 
        char_dec = int(char_bin, 2) 
        output_string += chr(char_dec)
    
    ### ---------- output string to text file ---------- ### 
    file = open('outputs\\output_message.txt', 'w') 
    file.write(output_string) 

decode() 
