# -*- coding: utf-8 -*-
"""
@author: Christina Hernandez Wunsch <hernandezwunschc@gmail.com>
"""

import unittest
from imaged.downloader import ImageDownloader

class ImageDownloaderTest(unittest.TestCase):
    def test_url_exists(self):
        ID = ImageDownloader("example.txt")
        # test for name/ service not found
        url_1 = 'http://somewebsrv.com/img/992147.jpg'
        self.assertFalse(ID.url_exists(url_1))
        # test for existing image
        url_2 = 'https://imgs.xkcd.com/comics/the_history_of_unicode.png'
        self.assertTrue(ID.url_exists(url_2))
    
    def test_get_image(self):
        ID = ImageDownloader("example.txt")
        url_3 = 'http://mywebserver.com/images/271947.jpg'
        ID.get_image(url_3)
        import os.path
        expected_image = '../images/example/271947.jpg'
        self.assertTrue(os.path.isfile(expected_image))
        
    
    def test_check_image(self):
        ID = ImageDownloader("example.txt")
        # test for image
        url_4 = 'https://imgs.xkcd.com/comics/the_history_of_unicode.png'
        self.assertTrue(ID.check_image(url_4))
        # test gif
        url_5 = 'https://media.giphy.com/media/aQbsSvYK7Jyfe/giphy.gif'
        self.assertTrue(ID.check_image(url_5))
        # test for pdf
        url_6 = 'http://robotics.stanford.edu/people/nilsson/MLBOOK.pdf'
        self.assertFalse(ID.check_image(url_6))
        # test simple html
        url_7 = 'https://deeplearning4j.org/lstm.html'
        self.assertFalse(ID.check_image(url_7))
        
    
if __name__ == "__main__": 
    unittest.main()
