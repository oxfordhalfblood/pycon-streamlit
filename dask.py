import dask
import dask_image.imread
import dask_image.ndfilters
import dask_image.ndmeasure
import dask.array as da
import matplotlib.pyplot as plt
import os
from skimage import data, io

# # from dask_image import ndmorph
# import numpy as np
# struc_elem = np.array([
#     [0,1,0,1,0],
#     [1,0,0,1,1],
# ])



output_filename = os.path.join('temp', 'astronaut.png')
io.imsave(output_filename, data.astronaut())
astronaut = dask_image.imread.imread(filename)
print(astronaut)
plt.imshow(astronaut[0, ...])  # display the first (and only) frame of the image