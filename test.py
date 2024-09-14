import cv2
import os
import sys

print("Starting the image binarization process...")

try:
    print(f"Current working directory: {os.getcwd()}")

    if len(sys.argv) < 2:
        raise ValueError("Please provide the input image path as a command-line argument.")

    # Use absolute path for the input image
    input_image_path = os.path.abspath(sys.argv[1])
    print(f"Absolute input image path: {input_image_path}")

    # Check if the file exists
    if not os.path.exists(input_image_path):
        raise FileNotFoundError(f"The file does not exist: {input_image_path}")
    else:
        print("File exists.")

    # Set the output image path (using absolute path)
    output_image_path = os.path.abspath(os.path.join('images', 'output', 'binary_image.tif'))
    print(f"Absolute output image path: {output_image_path}")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    # Load the image with OpenCV
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(f"Failed to load the image. The file may be corrupted or not an image: {input_image_path}")

    print("Image loaded successfully.")

    # Apply simple thresholding
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    print("Thresholding applied.")

    # Save the binary image
    cv2.imwrite(output_image_path, binary_image)
    print(f"Binary image saved at: {output_image_path}")

    # Display the original and binary images
    cv2.imshow('Original Image', image)
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)

except FileNotFoundError as fnf_error:
    print(f"File Error: {fnf_error}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Ensure all OpenCV windows are closed even if an error occurs
    cv2.destroyAllWindows()
