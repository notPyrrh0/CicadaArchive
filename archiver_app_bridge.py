
# Just a script to bridge the UI and archiver 

import os
import sys
import requests
from subprocess import run, getstatusoutput

class ArchiveManagerV2(object):
    def __init__(self):
        pass

    # <!--Iterate over all files (Busy)-->
    def check_files(self):
        with open("src/ignoreFiles.txt", "r") as f:
            ignoredFiles = [files.strip("\n") for files in f.readlines()] 

    def updateFromRepo(self):
        try:
            # Ensure there's connection and git is instaled in the system
            requests.get("https://github.com/", timeout=5)
            exitcode, _ = getstatusoutput("git")


            if exitcode == 1:
                print(os.getcwd())

                os.chdir("CicadaArchive")
                # run("git pull origin master")
            else:
                raise Exception("git is not installed")
        except requests.exceptions.ConnectionError:
            return "Connection Error!" 

    # for subdir, dirs, files in os.walk("inputFiles"):
    #     for file in files:
    #         print(os.path.join(subdir, file))

ArchiveManagerV2().updateFromRepo()