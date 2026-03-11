def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    res = []
    for i in range(len(image)):
        gray = []
        for j in range(len(image[i])):
            gray.append(float((0.299 * image[i][j][0]) + (0.587 * image[i][j][1]) + (0.114 * image[i][j][2])))
        res.append(gray)
    return res
             