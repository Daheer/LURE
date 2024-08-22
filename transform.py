import os
from torchvision import transforms
from torchvision.io import read_image, write_jpeg
from PIL import Image

# Define the image folder
image_folder = '/home/ubuntu/LURE/train2014'

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to 480x640
    transforms.CenterCrop((224, 224))
])

# Function to process and save the image
def process_image(image_path):
    # Load image
    # image = read_image(image_path)
    image = Image.open(image_path)

    # Apply the transformation
    resized_image = transform(image)

    # Save the resized image back to the original path
    # write_jpeg(resized_image, image_path, quality=100)
    resized_image.save(image_path)

# Loop through all files in the image folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        image_path = os.path.join(image_folder, filename)

        try:
            process_image(image_path)
            print(f"Processed {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

print("All images processed.")
