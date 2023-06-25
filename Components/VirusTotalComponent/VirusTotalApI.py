import requests
import time
from flask import jsonify
#from ..ChatGPTComponent.OpenAI import search_custom_sentence 
class VirusTotalAPI:


    url = 'https://www.virustotal.com/vtapi/v2/url/report'

    apikey = '8690d4c0ac912a650d878de21caa7189b9d793c4c5f7c8e10258038a443f1ac8'
    
    fileUploadUrl = "https://www.virustotal.com/api/v3/files"
  #  file_url: 'https://www.virustotal.com/api/v3/files/{id};

    file_report_url = 'https://www.virustotal.com/vtapi/v2/file/report' # Pull Report on the file hash.

    scan_url = 'https://www.virustotal.com/vtapi/v2/url/scan'

###
# Paramateres I want
#  Take the PermaLink (link to VirusTotal API)
# Positives (any hits)
# resource
# scan_date
#scan_id
# scans (iterate over this and print them) If they are cleansite unrated site and bad
# 
###


    def retrieveURLs(encoded_string): 
           params = {'apikey': VirusTotalAPI.apikey, 'resource': encoded_string} # from docs
           response = requests.get(VirusTotalAPI.url, params=params) 
           print(response.json())# Parse JSON data into a dictionary 
           return(response.json())
           #DataToQuery = jsonify(json_data)
          # ChatGPT = search_custom_sentence(DataToQuery)
       
    def retrieveProcess(file):
        params = {'apikey': VirusTotalAPI.apikey, 'resource': file}
        response = requests.get(VirusTotalAPI.file_report_url, params=params)
        json_data = response.json()   ## Parse JSON data into a dictionary
        return jsonify(json_data)
      
 