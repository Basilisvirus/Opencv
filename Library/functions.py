"""
Functions created by Christianidis Vasileios
email: basilisvirus@hotmail.com
inform me for any bugs, i am open to suggestions and new functions
"""

"""
This function takes two images as parameters, finds out which one has
the largest rows and cols and crops it, to fit the smallest image. in
the output (return), it returns both of the images, on their new,
smallest-image size.
"""
def same_size(img1, img2):
    # take the rows/cols of the images
    rows1, cols1 = img1.shape[:2]
    rows2, cols2 = img2.shape[:2]

    # change size of the biggest image, to be the same as the small one,
    # using image ROI:
    if cols1 < cols2:
        img2 = img2[0:rows2, 0:cols1]
    elif cols1 > cols2:
        img1 = img1[0:rows1, 0:cols2]
    if rows1 < rows2:
        img2 = img2[0:rows1, 0:cols2]
    elif rows1 > rows2:
        img1 = img1[0:rows2, 0:cols1]
    # return the same-sized images to the corresponding images
    return img1, img2


"""
This function takes as an input a image and checks if it has an odd
number of rows or columns. if it doesnt have a even number of either
rows or cols, it adds one col or row to make them even. 
The second parameter is a flag that decides if the odd image will increase
in size (+1) if flag='INC' or will decrease in size (-1) if flag= 'DEC'
"""
def even_resize(img, flag='INC'):
    # decides weather the odd image will increase in size or decrease in size.
    if flag == 'INC':
        k = 1
    elif flag == 'DEC':
        k = -1
    else:
        print('even_resize flag not defined, loading default')
        k = 1

    # take the rows/cols if the image
    rows, cols = img.shape[:2]  # rows, cols

    # divide the cols/rows by 2, using mod. if the result is 1, add one row/col
    if rows % 2:
        img = cv2.resize(img, (rows + k, cols))

    if cols % 2:
        img = cv2.resize(img, (rows, cols + k))
    # return the even rows/cols img
    return img


"""
This function creates and appends a laplacian pyramid (from smaller to larger image)
First parameter -in string- is the image file.Second parameter is a already-created 
(suggested to be empty) array, where the laplacian pyramid will be apended. 
Third parameter is the layers (how many images) sould be used for the pyramid 
(so 6 layers means 6 appends in the list).
Example of use:
random_list= []
laplacian_pyr('orange.jpg', lap, 8)
"""
def laplacian_pyr(filename, lap_array, layers=6):
    # read an image. image is read in BGR order
    img = cv2.imread(filename)

    # since the first position of the gaussian[] list will be used (see below code),
    # we need to increase the actual layers buy 1 position.
    layers = layers + 1

    # now create the gaussian pyramid
    # this helps creating a loop that will make the gaussian pyramid
    gaussian = [img]

    for i in range(layers):
        G = cv2.pyrDown(gaussian[i])
        gaussian.append(G)

    """ 
    Hi, i just wanted to reming you NOT to use this line. if you do,
    python will make a new array and wont save the images on the one
    outside the function
    lap_array = [] #dont use
    """
    # now create the laplacian pyramid
    # for i in range(from 5 to 0 with step -1) if we print(i), the output will be '5 4 3 2 1'
    for i in range(layers - 1, 0, -1):
        G = cv2.pyrUp(gaussian[i + 1])

        # check of the two images match in size.
        G, gaussian[i] = sizeFix(G, gaussian[i])
        res = cv2.subtract(gaussian[i], G)
        lap_array.append(res)
