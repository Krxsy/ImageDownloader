# -*- coding: utf-8 -*-
"""
@author: Christina Hernandez Wunsch <hernandezwunschc@gmail.com>
"""

import urllib.request
import urllib.error
import sys
import os

class ImageDownloader():
    """
    Takes a plaintext file consisting of URLs as an argument and downloads 
    all images, storing them on the local hard disk.
    """
    def __init__(self, file_name):
        """
        filename: str
                plaintext file from which we want the images from
        """
        self.file_name = file_name
        self.output = '../images/%s' %file_name.split('/')[-1].split('.')[0]
        if not os.path.exists(self.output):
            os.makedirs(self.output)
    
    def url_exists(self, url):
        """
        Checks if the given URL is reachable
        """
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        try:
            urllib.request.urlopen(request)
            return True
        except urllib.error.URLError as e:
            print("%s for %s" %(e.reason, url))
            return False
    
    def check_image(self, url):
        """
        Checks if url is actually an image 
        (only for png, gif, jpg, and jpeg, as these are the only 
        formats we are likely to encounter).
        """
        if any(ex in url.lower() for ex in ['.png', '.gif', '.jpg', '.jpeg']):
            return True
        else:
            return False
            
        
          
    def get_image(self, url):
        """
        Retrieves the image from the url
        """
        img_name = url.split('/')[-1]
        img_name = img_name.strip('\n')
        print('Getting %s' %img_name)
        output_file = self.output + '/%s'%img_name
        urllib.request.urlretrieve(url, output_file)
        
    
    def parser(self):
        """
        Reads in a plaintext file, extracts images and stores them on 
        local hard disk: ../images
        """
        with open(self.file_name) as file:
            for line in file:
                print('check',self.check_image(line))
                if self.url_exists(line) and self.check_image(line):
                    self.get_image(line)
                    
                        
                
                
                
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 downloader.py <file>")
        sys.exit()
    file_name = sys.argv[1] 
    img_downloader = ImageDownloader(file_name)
    img_downloader.parser()
    print("Successfully downloaded all available images into %s" %img_downloader.output)           
                
            
        