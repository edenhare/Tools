# ----------
# checklinks.py
# 
# this tool takes a URL as an argument and parses the page 
# looking for other links.

import requests
from html.parser import HTMLParser
from html.entities import name2codepoint
import sys

links = []          # store the links which are found
base = []           # store the base href if found
bad = []            # list of bad URLs
linkcheck = []      # links we have processed
count = 0           # number of links processed
good = 0            # number of good links
skipped = 0         # number of skipped links
fail = 0            # number of bad links

def get_url(**kwargs):
    
    # 
    # refer to all of the global variables so we can use them
    #
    global count
    global good
    global fail
    global skipped
    global bad
    global linkcheck
    response = ""
    
    #
    # get the url we are going to process from the arguments
    # 
    target = kwargs['url']
    
    if target in linkcheck:
        #
        # if the link has been processed, don't check it again
        #
        response = ""
    else:
        #
        # process the link
        #
        print(f"URL: {target} ... ", end='', flush=True)
        data = requests.get(target)
        response = data.text
        #
        # check the extension
        # We know some files will not have links to check, like
        # audio files, image files, so return nothing to the caller
        #
        index = target.rfind('.')
        extension = target[index + 1:]
        
        if extension == "mp3":
            response = ""
        elif extension == "png":
            response = ""
        elif extension == "jpg":
            response = ""
        elif extension == "jpeg":
            response = ""

        count+=1
        if data.status_code == 200:
            print(" [OK]")
            good+=1
        elif data.status_code == 999:
            print(" [SKIPPED]")
            skipped+=1
        else:
            print(f" [{data.status_code}]")
            bad.append(target)
            fail+=1
        
    return response
    

class MyHTMLParser(HTMLParser):
        
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for name, value in attrs:
               if name == "src":
                       links.append(value)
        elif tag == "source":
            for name, value in attrs:
               if name == "src":
                       links.append(value)
        elif tag == "a":
            for name, value in attrs:
               if name == "href":
                   if value.find("mailto:") == -1:
                       links.append(value)
        elif tag == "base":
           for name, value in attrs:
               if name == "href":
                   base.append(value)


def main():
    
    global linkcheck
    
    #
    # Print who we are
    #
    print(f"Running as {sys.argv[0]}")
    
    #
    # Validate if we have any arguments
    #
    if len(sys.argv) < 2:
        #
        # No template on comand line, quit
        #
        print(f"Usage: {sys.argv[0]} starting-url")
        sys.exit(1)
    
    top = sys.argv[1]    
    #top = "http://labrlearningweb.s3-website-us-east-1.amazonaws.com/index.html"
    
    root = get_url(url=top)
    parser = MyHTMLParser()
    parser.feed(root)
    
    print(f"Base URL: {base}")
    print(links)
    
    for link in links:
        if link.find("http",0) == -1:
            link = base[0] + link
    
        page = get_url(url=link)
        linkcheck.append(link)
        if link.find(base[0]) == 0:
            parser = MyHTMLParser()
            parser.feed(page)
        else:
            pass
        
    print("\nBad links")
    for link in bad:
        print(link)
    
    print("\nSummary")
    print(f"Total links processed: {count}")
    print(f"Valid links: {good}")
    print(f"Invalid links: {fail}")
    print(f"Skipped links: {skipped}")    

if __name__ == "__main__":
    main()
    
    
