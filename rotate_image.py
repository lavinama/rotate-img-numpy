import numpy as np

def change_angle_to_radius_unit(angle):
    angle_radius = angle * (np.pi/180)
    return angle_radius

def rotate(src_img, angle_of_rotation, pivot_point):
    """Rotate image by angle using numpy

    :param image: np.array of shape (height, width, channels)
    :param angle: value of rotation clockwise in radians
    :return: rotated image
    """
    # get image shape
    height, width, channels = src_img.shape
    # 1. Create rotation matrix
    rotation_mat = np.transpose(np.array([[np.cos(angle_of_rotation),-np.sin(angle_of_rotation)],
                            [np.sin(angle_of_rotation),np.cos(angle_of_rotation)]]))
    pivot_point_x =  pivot_point[0]
    pivot_point_y = pivot_point[1]
    rotated_image = np.zeros(src_img.shape,dtype='u1') 

    for h in range(height): #h = number of row
        for w in range(width): #w = number of col
            # 2. For each pixel in the image, calculate the new position of the pixel
            xy_mat = np.array([[h - pivot_point_x],[w - pivot_point_y]])
            rotate_mat = np.dot(rotation_mat,xy_mat)
            new_x = pivot_point_x + int(rotate_mat[0])
            new_y = pivot_point_y + int(rotate_mat[1])
            # 3. If the new position is within the image, copy the pixel value to the new position
            if (0<=new_x<=w-1) and (0<=new_y<=h-1): 
                rotated_image[new_y,new_x] = src_img[height,width]

    return rotated_image