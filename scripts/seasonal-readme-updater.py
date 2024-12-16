import os
from datetime import datetime

# dictionary mapping dates/periods to special images
SEASONAL_IMAGES = {
    # holidays
    "1031": "halloween.png",
    "0908": "birthday.png",
    "2204": "earthday.png",
    "0701": "programmersday.png",
    
    # holiday seasons
    "1220-1225": "christmas.png",
    "3112-0101": "newyear.png",
    # "0825-0827": "onam.png",
}

def get_current_seasonal_image(default_image="header.png"):
    """
    Determine the appropriate image based on current date
    
    Args:
        default_image (str): Default image to use if no seasonal image matches
    
    Returns:
        str: Filename of the image to use
    """
    today = datetime.now()
    today_str = today.strftime("%m%d")
    
    # check for exact date matches first
    if today_str in SEASONAL_IMAGES:
        return SEASONAL_IMAGES[today_str]
    
    # check for date ranges
    for date_range, image in SEASONAL_IMAGES.items():
        if "-" in date_range:
            start_date, end_date = date_range.split("-")
            if start_date <= today_str <= end_date:
                return image
    
    return default_image

def update_readme(image_filename):
    """
    Update README.md with the new image path
    
    Args:
        image_filename (str): Filename of the image to use
    """
    readme_path = "README.md"
    
    with open(readme_path, 'r') as file:
        content = file.read()
    
    # replace the image path in the README
    updated_content = content.replace("header.png", image_filename)
    
    with open(readme_path, 'w') as file:
        file.write(updated_content)
    
    print(f"README updated with {image_filename}")

def main():
    # path to dependencies folder containing images
    dependencies_folder = os.path.join(os.path.dirname(__file__), '..', 'dependencies')

    # get the seasonal image
    seasonal_image = get_current_seasonal_image()
    
    # full path to the image
    image_path = os.path.join(dependencies_folder, seasonal_image)
    
    # update README
    update_readme(seasonal_image)

if __name__ == "__main__":
    main()
