import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import getopt
import argparse

def main(argv):
   url = ''
   cmstype = ''
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hu:o:",["url=","outputfile=","cmstype"])
   except getopt.GetoptError:
      print ('loggen_create_urls.py -u <url> -o <outputfile> -c <basic> or <wordpress>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('use loggen_create_urls.py -u <url to crawl> -o <output file to store crawled urls> -c <basic website or wordpress site>')
         sys.exit()
      elif opt in ("-u", "--url"):
         url = arg
      elif opt in ("-o", "--outputfile"):
         outputfile = arg
      elif opt in ("-c", "--cmstype"):
         outputfile = arg
   print ('Url to crawl is "', url)
   print ('Output file is "', outputfile)
   print ('cmstype file is "', cmstype)
''' extract_links(url) '''

links = []
df = pd.DataFrame({"links":links})
df.to_csv("links.csv")
def extract_links(url):
    print("source url",url)
    global links

    source_url = requests.get(url)
    soup = BeautifulSoup(source_url.content,"html.parser")
    for link in soup.find_all('a',href=True, recursive=True):
        try:
            if len(links) >=100:
                return
            if link.get('href').startswith(url) and link.get("href") not in links:
                links.append(link.get('href'))
                extract_links(link.get('href'))

        except Exception as e:
            print("Unhandled exception",e)


if __name__ == "__main__":
   main(sys.argv[1:])