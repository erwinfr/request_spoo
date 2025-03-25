import sys
import random
from datetime import datetime, timedelta
import socket
import struct
import os 
import json
import csv
import ipaddress
import codecs

random_ip = str( ipaddress.IPv4Address( random.randint( 0, 4294967295 ) ) )
open_connect = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0100")
filler1 = " - - ["
filler2 = "] "
print(random_ip) 
# Assisted by watsonx Code Assistant 
with open('/Users/erwin/Documents/Projecten/PTI/dev/deb_pod/input.txt', 'r' ) as input_file, codecs.open('/Users/erwin/Documents/Projecten/PTI/dev/deb_pod/output.log', 'w', "utf-8-sig") as output_file:
    for line in input_file:
        random_ip2 = str( ipaddress.IPv4Address( random.randint( 0, 4294967295 ) ) ) 
        modified_line = line.replace(line[:47], "cp4s.cool8.nl "+"httpd: "+random_ip2+" 185.87.187.124"+filler1+open_connect+filler2)
        output_file.write(modified_line)
        print(random_ip2)
    output_file.close()