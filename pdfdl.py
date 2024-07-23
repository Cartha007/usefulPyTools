# TODO = Add logging

import os
import requests
from urllib.parse import urlsplit


def download_pdf(url, save_directory):
    response = requests.get(url)
    
    
    if response.status_code == 200:
    # Attempt to get the filename from the Content-Disposition header
        if 'Content-Disposition' in response.headers:
            content_disposition = response.headers['Content-Disposition']
            if 'filename=' in content_disposition:
                filename = content_disposition.split('filename=')[-1].strip('"')
            else:
                filename = os.path.basename(urlsplit(url).path)
        else:
            # Fallback to extracting the filename from the URL
            filename = os.path.basename(urlsplit(url).path)
            
            
        # Create the full save path
        save_path = os.path.join(save_directory, filename)
        # Ensure the save directory exists
        os.makedirs(save_directory, exist_ok=True)
        
        
        with open(save_path, 'wb') as f:
            f.write(response.content)
            
        print(f"Successfully downloaded {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        
def main():
    url = input("Enter url:")
    save_directory = "downloads"


    download_pdf(url, save_directory)
    
    
if __name__ == "__main__":
    main()