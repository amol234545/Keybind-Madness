import zipfile
import os
import requests
import pathlib


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename
path = download_file(requests.get(requests.get(requests.get("https://api.github.com/repos/UpliftGames/wally/releases").json()[0].get("assets_url")).json()[0].get("url")).json().get("browser_download_url"))
zip = zipfile.ZipFile(path,"r")
folder_path = str(path).split(".zip")[0]
zip.extractall(folder_path)
os.system(pathlib.Path(folder_path).joinpath("wally").__str__() + " install")