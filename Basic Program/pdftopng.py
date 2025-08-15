from pdf2image import convert_from_path
import os

# Path to the uploaded PDF
pdf_path = "/mnt/data/The redemption arc.pdf"

# Convert PDF to images
images = convert_from_path(pdf_path)

# Save each page as an image
output_files = []
for i, image in enumerate(images):
    image_path = f"/mnt/data/page_{i+1}.png"
    image.save(image_path, "PNG")
    output_files.append(image_path)

output_files
