import numpy as np
arrayTextureCamouflage = np.load('textures/texture_camouflage.npy')
print(f'arrayTextureCamouflage.shape: {arrayTextureCamouflage.shape}')
# arrayTrainData = np.load('carla_dataset/train/data1.npz')
# print(f'arrayTrainData.shape: {arrayTrainData.shape}')

import zipfile
def npz_headers(npz):
    """
    Takes a path to an .npz file, which is a Zip archive of .npy files.
    Generates a sequence of (name, shape, np.dtype).
    """
    with zipfile.ZipFile(npz) as archive:
        for name in archive.namelist():
            if not name.endswith('.npy'):
                continue

            npy = archive.open(name)
            version = np.lib.format.read_magic(npy)
            shape, fortran, dtype = np.lib.format._read_array_header(npy, version)
            yield name[:-4], shape, dtype
print(npz_headers('carla_dataset/train/data1.npz')) 