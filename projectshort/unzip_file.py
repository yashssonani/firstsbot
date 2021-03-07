import asyncio
import os
import shutil
import zipfile
import time
import tarfile



async def create_unzip(input_directory):
    #return_name = None
    working_directory = os.path.dirname(os.path.abspath(input_directory))
    new_working_directory = os.path.join(
        working_directory,
        str(time.time())
    )
    new_working_directory = new_working_directory 
    if not os.path.isdir(new_working_directory):
        os.makedirs(new_working_directory)
        return_name = new_working_directory
        if ".tar" in input_directory:
           my_tar = tarfile.open(input_directory)

           extract_file = my_tar.extractall(new_working_directory) 

           my_tar.close() 
           
        if ".zip" in input_directory:
           target = input_directory
           handle = zipfile.ZipFile(target)
        
           extract_file = handle.extractall(new_working_directory)
           handle.close
        
     
        
    return return_name