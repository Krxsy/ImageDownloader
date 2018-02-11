# ImageDownloader

A script that takes a plaintext file as an argument and downloads all images, storing them on the local hard disk.

plaintext file (containing URLs) looks like this:

http://mywebserver.com/images/271947.jpg <br />
http://mywebserver.com/images/24174.jpg <br />
http://somewebsrv.com/img/992147.jpg <br />

Usage
-----

Simply run:

    >>> python3 downloader.py <file>

e.g.
    >>> python3 downloader.py ../tests/example.txt

In this case, the downloaded images can be found in ImageDownloader/images/example
