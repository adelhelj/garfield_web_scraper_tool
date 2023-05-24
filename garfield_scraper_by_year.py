import requests
from bs4 import BeautifulSoup
import os

# Base URL of the website
base_url = 'http://pt.jikos.cz/garfield/'

# Create a directory to save the images
if not os.path.exists('garfield_images'):
    os.makedirs('garfield_images')

# Loop over the desired years (from 1978 to 2023)
for year in range(1978, 2024):
    # Counter variable to track the image number
    counter = 1

    # URL for the specific year
    url = f'{base_url}{year}/'

    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the image tags on the page
    image_tags = soup.find_all('img')

    # Create a directory for the specific year
    year_directory = os.path.join('garfield_images', str(year))
    if not os.path.exists(year_directory):
        os.makedirs(year_directory)

    # Download and save each image
    for image_tag in image_tags:
        image_url = image_tag['src']
        if not image_url.startswith('http'):
            image_url = url + image_url
        image_extension = image_url.split('.')[-1]
        image_name = f'{year}_{counter}.{image_extension}'
        image_path = os.path.join(year_directory, image_name)
        response = requests.get(image_url)
        with open(image_path, 'wb') as f:
            f.write(response.content)
            print(f'Saved image: {image_path}')
        counter += 1
