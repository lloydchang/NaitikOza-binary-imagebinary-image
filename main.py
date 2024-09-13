import cv2
import numpy as np
import os

print("Starting the image binarization process...")

# Paths for input and output images
input_image_path = os.path.join('images', 'input', '1_binary.tif')
output_image_path = os.path.join('images', 'output', 'binary_image.tif')

try:
    # Print the input image path for debugging
    print(f"Input image path: {input_image_path}")
    
    # Load the image with OpenCV
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was loaded successfully
    if image is None:
        raise FileNotFoundError(f"File not found or cannot be read: {input_image_path}")
    
    print("Image loaded successfully.")

    # Apply simple thresholding
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    print("Thresholding applied.")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    # Save the binary image
    cv2.imwrite(output_image_path, binary_image)
    print(f"Binary image saved at: {output_image_path}")

    # Display the original and binary images
    cv2.imshow('Original Image', image)
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as fnf_error:
    print(f"File Error: {fnf_error}")

except Exception as e:
    print(f"Error: {e}")


