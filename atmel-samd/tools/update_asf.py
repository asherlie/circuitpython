import requests
import zipfile
import os.path
import sys

for chip in ["samd21", "samd51"]:
    r = None
    filename = chip + ".zip"
    if not os.path.isfile(filename):
        with open("tools/" + chip + ".json", "r") as project_json:
            headers = {"content-type": "text/plain"}
            r = requests.post("http://start.atmel.com/api/v1/generate/?format=atzip&compilers=[make]&file_name_base=My%20Project", headers=headers, data=project_json)
        if not r.ok:
            # Double check that the JSON is minified. If its not, you'll get a 404.
            print(r.text)
            sys.exit(1)
        with open(filename, "wb") as out:
            out.write(r.content)
    z = zipfile.ZipFile(filename)
    z.extractall("asf4/" + chip)
    print(z)

    # delete the zip on success
    os.remove(filename)


# samd21/samd21a/include is copied to samd21/include to match samd51
