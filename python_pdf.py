
# import datetime
# import fitz  # PyMuPDF
# import os
# from PIL import Image  # Pillow
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas

# def pdf2img(pdf_path, img_path, output_pdf_path):
#     # Open the PDF file
#     pdfDoc = fitz.open(pdf_path)
    
#     # Get the PDF file name (without extension)
#     pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
#     # Ensure the output folder exists
#     if not os.path.exists(img_path):
#         os.makedirs(img_path)
    
#     # List to store paths of all generated images
#     image_files = []
    
#     # Iterate through each page
#     for page_num, page in enumerate(pdfDoc.pages(), start=1):
#         # Set zoom and rotation parameters
#         rotate = int(0)
#         zoom_x = 0.8
#         zoom_y = 0.8
#         mat = fitz.Matrix(zoom_x, zoom_y)
        
#         # Get the image of the current page
#         pix = page.get_pixmap(matrix=mat, dpi=120, colorspace='rgb', alpha=False)
        
#         # Generate image file name: PDFName_pageNumber.png
#         image_name = f"{pdf_name}_page{page_num}.png"
#         target_img_name = os.path.join(img_path, image_name)
        
#         # Save the image
#         pix.save(target_img_name)
#         image_files.append(target_img_name)
#         print(f"Saved: {target_img_name}")
    
#     # Merge all images into a single PDF
#     images_to_pdf(image_files, output_pdf_path)
#     print(f"Merged PDF generated: {output_pdf_path}")

# def images_to_pdf(image_files, output_pdf_path):
#     # Create a PDF file
#     c = canvas.Canvas(output_pdf_path, pagesize=A4)
    
#     for image_file in image_files:
#         # Open the image
#         img = Image.open(image_file)
#         img_width, img_height = img.size
        
#         # Set PDF page size to match the image size
#         c.setPageSize((img_width, img_height))
        
#         # Add the image to the PDF page
#         c.drawImage(image_file, 0, 0, width=img_width, height=img_height)
#         c.showPage()  # End the current page
    
#     # Save the PDF
#     c.save()

# if __name__ == '__main__':
#     startTime_pdf2img = datetime.datetime.now()  
#     pdf_path = "C:\\PDFDEMO\\2_1.PDF"
#     img_path = "C:\\PDFDEMO\\img"
#     output_pdf_path = "C:\\PDFDEMO\\output.pdf"  # Path for the merged PDF file

#     # Call the function
#     pdf2img(pdf_path, img_path, output_pdf_path)

#     endTime_pdf2img = datetime.datetime.now() 
#     print('===========END==========')
#     print('Total time taken: %d seconds' % (endTime_pdf2img - startTime_pdf2img).seconds)

import datetime
import fitz  # PyMuPDF
import os
from PIL import Image  # Pillow
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def pdf2img(pdf_path, img_path, output_pdf_path, dpi=120):
    # Open the PDF file
    pdfDoc = fitz.open(pdf_path)
    
    # Get the PDF file name (without extension)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Ensure the output folder exists
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    
    # List to store paths of all generated images
    image_files = []
    
    # Iterate through each page
    for page_num, page in enumerate(pdfDoc.pages(), start=1):
        # Set zoom and rotation parameters
        rotate = int(0)
        zoom_x = 0.8  # Adjust zoom for better resolution
        zoom_y = 0.8
        mat = fitz.Matrix(zoom_x, zoom_y)
        
        # Get the image of the current page
        pix = page.get_pixmap(matrix=mat, dpi=dpi, colorspace='rgb', alpha=False)
        
        # Generate image file name: PDFName_pageNumber.png
        image_name = f"{pdf_name}_page{page_num}.png"
        target_img_name = os.path.join(img_path, image_name)
        
        # Save the image
        pix.save(target_img_name)
        
        # Compress the image using Pillow
        compress_image(target_img_name)
        
        image_files.append(target_img_name)
        print(f"Saved: {target_img_name}")
    
    # Merge all images into a single PDF
    images_to_pdf(image_files, output_pdf_path)
    print(f"Merged PDF generated: {output_pdf_path}")

def compress_image(image_path, quality=50):
    """
    Compress an image to reduce file size.
    :param image_path: Path to the image file.
    :param quality: Quality of the compressed image (0-100).
    """
    img = Image.open(image_path)
    img.save(image_path, optimize=True, quality=quality)

def images_to_pdf(image_files, output_pdf_path):
    # Create a PDF file
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    
    for image_file in image_files:
        # Open the image
        img = Image.open(image_file)
        img_width, img_height = img.size
        
        # Set PDF page size to match the image size
        c.setPageSize((img_width, img_height))
        
        # Add the image to the PDF page
        c.drawImage(image_file, 0, 0, width=img_width, height=img_height)
        c.showPage()  # End the current page
    
    # Save the PDF
    c.save()

if __name__ == '__main__':
    startTime_pdf2img = datetime.datetime.now()  
    pdf_path = "C:\\PDFDEMO\\2_1.PDF"
    img_path = "C:\\PDFDEMO\\img"
    output_pdf_path = "C:\\PDFDEMO\\output.pdf"  # Path for the merged PDF file

    # Call the function
    pdf2img(pdf_path, img_path, output_pdf_path, dpi=100)  # Adjust DPI as needed

    endTime_pdf2img = datetime.datetime.now() 
    print('===========END==========')
    print('Total time taken: %d seconds' % (endTime_pdf2img - startTime_pdf2img).seconds)