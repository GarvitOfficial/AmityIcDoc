import cv2
import streamlit as st
import numpy as np

def addText(name, enroll, image_file):
    # Read the image from the uploaded file
    image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), 1)

    # Check if the image is loaded correctly
    if image is not None:
        # Font settings
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Text 1: Name
        org_name = (775, 1270)  # Coordinates for name
        fontScale_name = 1
        color_name = (0, 0, 0)  # Black in BGR
        thickness_name = 2
        image = cv2.putText(image, name, org_name, font, fontScale_name, color_name, thickness_name, cv2.LINE_AA)
        
        # Text 2: Enrollment
        org_enroll = (645, 1380)  # Coordinates for enrollment number
        fontScale_enroll = 1
        color_enroll = (0, 0, 0)  # Black in BGR
        thickness_enroll = 2
        image = cv2.putText(image, enroll, org_enroll, font, fontScale_enroll, color_enroll, thickness_enroll, cv2.LINE_AA)
        
        # Convert BGR image to RGB for displaying with Streamlit
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Display the image using Streamlit
        st.image(image_rgb, caption="Image with Text", use_column_width=True)

        # Save the image with the enrollment number in the filename
        output_filename = f"image_with_{enroll}.png"  # Saving as PNG
        cv2.imwrite(output_filename, image)  # Save the image to disk
        
        # Add a download button for the image
        with open(output_filename, "rb") as file:
            st.download_button(
                label="Download Image with Text",
                data=file,
                file_name=output_filename,
                mime="image/png"
            )
        
        st.success(f"Image saved as {output_filename}")
    else:
        st.error("Image not found. Please check the path.")

# Streamlit UI
st.title("Add Text to Image")

# Take inputs from the user
name = st.text_input("Enter Name:")
enroll = st.text_input("Enter Enrollment Number:")

# Upload image file
image_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# Button to trigger the addText function
if st.button("Add Text"):
    if name and enroll and image_file:
        addText(name, enroll, image_file)
    else:
        st.error("Please fill in all fields and upload an image.")
