import os
from datetime import datetime

# Dictionary mapping dates/periods to special images
SEASONAL_IMAGES = {
    # Holidays
    "1031": "halloween.png",
    "0908": "birthday.png",
    "2204": "earthday.png",
    "0701": "programmersday.png",
    "1225": "christmas.png",
    
    # Holiday seasons (date ranges)
    "3112-0101": "newyear.png",
    # "0825-0827": "onam.png",
}

def get_current_seasonal_image(default_image="header.png"):
    """
    Determine the appropriate image based on the current date.
    
    Args:
        default_image (str): Default image to use if no seasonal image matches
    
    Returns:
        str: Filename of the image to use
    """
    today = datetime.now()
    today_str = today.strftime("%m%d")
    
    # Check for exact date matches first
    if today_str in SEASONAL_IMAGES:
        return SEASONAL_IMAGES[today_str]
    
    # Check for date ranges
    for date_range, image in SEASONAL_IMAGES.items():
        if "-" in date_range:
            start_date, end_date = date_range.split("-")
            if start_date <= today_str <= end_date:
                return image
    
    # If no match is found, return the default image (header.png)
    return default_image

def update_readme(image_filename):
    """
    Update README.md with the new image path.
    
    Args:
        image_filename (str): Filename of the image to use
    """
    readme_path = "README.md"
    
    with open(readme_path, 'r') as file:
        content = file.read()
    
    # Replace the image path in the README
    updated_content = content.replace("header.png", image_filename)
    
    with open(readme_path, 'w') as file:
        file.write(updated_content)
    
    print(f"README updated with {image_filename}")

def main():
    # Path to dependencies folder containing images
    dependencies_folder = os.path.join(os.path.dirname(__file__), '..', 'dependencies')

    # Get the seasonal image
    seasonal_image = get_current_seasonal_image()
    
    # Print current date and matching image
    today = datetime.now()
    print(f"Current date: {today.strftime('%d/%m')}, Matching header image: {seasonal_image}")
    
    # If seasonal image matches, proceed
    if seasonal_image != "header.png":
        # Full path to the seasonal image
        image_path = os.path.join(dependencies_folder, seasonal_image)
        
        # Update README
        update_readme(seasonal_image)
    else:
        print("No seasonal image for today. Using default header.png.")

if __name__ == "__main__":
    main()
