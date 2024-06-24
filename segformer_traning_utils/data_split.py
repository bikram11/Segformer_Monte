import os
import shutil
import random

# Define the paths to the folders
output_folder = '/home/bikram/Desktop/VIT_MODEL/SODA-20240621T133007Z-001/SODA/VICK_SYU_MODIFICATION'
train_folder = os.path.join(output_folder, 'train')
test_folder = os.path.join(output_folder, 'test')
val_folder = os.path.join(output_folder, 'val')

# Create the subfolders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# List all files in the output folder
all_files = [f for f in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, f))]

# Filter out mask files and pair them with their corresponding images
images = [f for f in all_files if not f.endswith('_mask.png')]
image_mask_pairs = [(img, img.replace('.jpg', '_mask.png')) for img in images]

# Shuffle the image-mask pairs to ensure randomness
random.shuffle(image_mask_pairs)

# Define split ratios
train_ratio = 0.7
test_ratio = 0.2
val_ratio = 0.1

# Calculate the number of pairs for each set
total_pairs = len(image_mask_pairs)
print(total_pairs)
train_count = int(total_pairs * train_ratio)
test_count = int(total_pairs * test_ratio)
val_count = total_pairs - train_count - test_count

# Split the pairs
train_pairs = image_mask_pairs[:train_count]
test_pairs = image_mask_pairs[train_count:train_count + test_count]
val_pairs = image_mask_pairs[train_count + test_count:]

# Function to copy files to the respective folder
def copy_files(pairs, destination_folder):
    for img, mask in pairs:
        src_img_path = os.path.join(output_folder, img)
        src_mask_path = os.path.join(output_folder, mask)
        dst_img_path = os.path.join(destination_folder, img)
        dst_mask_path = os.path.join(destination_folder, mask)

        
        if os.path.exists(src_img_path):
            shutil.copy(src_img_path, dst_img_path)
        if os.path.exists(src_mask_path):
            shutil.copy(src_mask_path, dst_mask_path)

# Copy pairs to the respective folders
copy_files(train_pairs, train_folder)
copy_files(test_pairs, test_folder)
copy_files(val_pairs, val_folder)

print(f"Files have been split into train, test, and val folders successfully.")
print(f"Train: {len(train_pairs)} pairs, Test: {len(test_pairs)} pairs, Val: {len(val_pairs)} pairs")
