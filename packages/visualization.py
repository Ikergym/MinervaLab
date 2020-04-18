def hex_to_rgb(number_hex):
    """This function converts a hexadecimal color to its rgb
    equivalent.
    
    Args:
        number_hex: String containing the hexadecimal representation
        of the color.\n
        
    Returns:
        number_rgb: Tuple consisted of the 3 numbers of the rgb
        representation of the color.\n
    """
    
    if '#' in number_hex:
        number_hex = number_hex[1:]
    
    number_rgb = (int(number_hex[0:2], 16), \
                  int(number_hex[2:4], 16), \
                  int(number_hex[4:], 16))
    
    return number_rgb


def rgb_to_hex(number_rgb):
    """This function converts a rgb color to its hexadecimal
    equivalent.
    
    Args:
        number_rgb: Tuple consisted of the 3 numbers of the rgb
        representation of the color.\n
        
    Returns:
        number_hex: String containing the hexadecimal representation
        of the color.\n
    """
    
    number_rgb = '#' \
    + format(number_rgb[0], '02x') \
    + format(number_rgb[1], '02x') \
    + format(number_rgb[2], '02x')
    
    return number_rgb


def generate_gradient(initial, final, length):
    """This function generates a color gradient consisted of N
    colors from the initial to the final.
    
    Args:
        initial: String of the hexadecimal representation of the
        initial color.\n
        final: String of the hexadecimal representation of the
        final color.\n
        length: Number of colors.\n
        
    Returns:
        colors: List consisted of strings of the hexadecimal
        colors.\n
    """
    
    i_r, i_g, i_b = hex_to_rgb(initial)
    f_r, f_g, f_b = hex_to_rgb(final)
    
    r_step = (f_r - i_r)/length
    g_step = (f_g - i_g)/length
    b_step = (f_b - i_b)/length
    
    r, g, b = i_r, i_g, i_b
    colors = []
    
    for i in range(length):

        h = rgb_to_hex((int(round(r)),int(round(g)),int(round(b))))
        
        colors.append(h)
        
        r = r + r_step
        g = g + g_step
        b = b + b_step

    return colors