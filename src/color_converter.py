import webcolors

def get_closest_color(requested_color) -> str:

    requested_color = webcolors.hex_to_rgb(requested_color)

    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    closest_color = min_colours[min(min_colours.keys())]

    return closest_color