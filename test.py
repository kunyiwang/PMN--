import rawpy
import sys
import numpy as np

if __name__ == '__main__':

    # Part 1: check why reading RAW image failed with TooBigFile error
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

    # Trying to add a seperator in logs file
    separator = "KUNYI---------------KUNYI---------------KUNYI\n"
    # Then write the separator to your log file
    with open('./logs/log_SonyA7S2_Mix_Unet.log', 'a') as f:
        f.write(separator)
        # Now, when you write the next log entry, it will start on a new line.
