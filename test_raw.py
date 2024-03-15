import rawpy
import sys
import numpy as np

if __name__ == '__main__':
    # path = './data/ELD/SonyA7S2/scene-1/IMG_0001.ARW'
    # path = './data/SID/Sony/long/00001_00_10s.ARW'
    path = './data/SID/Sony/long/20005_00_10s.ARW'

    try:
        data = rawpy.imread(path).raw_image_visible
        print(f"Shape of the RAW image data: {data.shape}")
        H = 2848
        W = 4256
        hr_raw = np.array(data).reshape(H, W)
        print(f"Successfully reshaped the RAW image data to shape: {hr_raw.shape}")
    except Exception as e:
        print(f"Error processing {path}: {e}")
