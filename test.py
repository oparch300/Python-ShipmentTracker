import csv
import pandas as pd
from stamps.config import StampsConfiguration
from stamps.services import StampsService
import logging
import os
import sys

sys.path.insert(1,'E:/ShipmentTracker')

logging.basicConfig()
logging.getLogger("suds.client").setLevel(logging.DEBUG)
file_path = os.path.abspath('ShipmentTracker')
print(file_path)
directory_path = os.path.dirname(file_path)
print(directory_path)
file_name = os.path.join(directory_path, "tests.cfg")
CONFIGURATION = StampsConfiguration(wsdl="testing", file_name='file_name')



# Read csv
TrackerIDs = []
data = pd.read_csv('E:/ShipmentTracker/ex.csv')
TrackerIDs.append(data['ID'])

Address = []
# Get Track of ID  and Write to a csv
for i in range(len(TrackerIDs)):
    #service = StampsService(CONFIGURATION)
   # Address.append(service.get_tracking(TrackerIDs[i]))
  print("hi")

#Write to csv
with open('E:/ShipmentTracker/output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(Address)
