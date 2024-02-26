from PIL import Image 
import numpy as np
import sys
import os
depthValue = 10.
rawSourcePath = os.path.realpath("./input.jpg")
rawOutputPath = os.path.realpath("./output.jpg")
if (len(sys.argv) > 1):
    depthValue = sys.argv[1]
if (len(sys.argv) > 2) :
    rawSourcePath = os.path.realpath(sys.argv[2])
if (len(sys.argv) > 3) :
    rawOutputPath = sys.argv[3]
depth = float(depthValue)
a = np.asarray(Image.open(rawSourcePath, "r").convert('L')).astype('float')
grad = np.gradient(a)
grad_x, grad_y = grad
grad_x = grad_x * depth / 100. 
grad_y = grad_y * depth / 100. 
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.) 
uni_x = grad_x / A 
uni_y = grad_y / A 
uni_z = 1. / A 

vec_el = np.pi / 2.2
vec_az = np.pi / 4. 
dx = np.cos(vec_el) * np.cos(vec_az)
dy = np.cos(vec_el) * np.sin(vec_az)
dz = np.sin(vec_el)

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z) 
b = b.clip(0, 255) 
im = Image.fromarray(b.astype('uint8'))
im.save(rawOutputPath)
print("input: ", rawSourcePath, "depth: ", depth, "output: ", rawOutputPath)
