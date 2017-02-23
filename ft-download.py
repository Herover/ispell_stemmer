import sys
import json
import requests

url = sys.argv[2]
more = True
while more:
    print(url)
    r = requests.get(url)
    if r.status_code != 200:
        print(r.status_code)
        break
    j = r.json()
    for item in j["value"]:
        print(item["titel"])

        # Verify filurl
        if item["filurl"] == "":
            print("Tom filurl")
            continue
            
        document_request = requests.get(item["filurl"])

        # Fix extension, everything is pdfs
        if not item["titel"].endswith(".pdf"):
            ext = ".pdf"
        else:
            ext = ""
        
        with open(sys.argv[1] + str(item["id"]) + "-" + item["titel"][0:20] + ext, "wb") as fd:
            for chunk in document_request.iter_content(chunk_size=128):
                fd.write(chunk)
    if "odata.nextLink" in j:
        more = True
        url = j["odata.nextLink"]
    else:
        more = False
        print("No more")
        
