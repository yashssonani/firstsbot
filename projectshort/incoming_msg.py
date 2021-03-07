import asyncio
import os
import time
import pyrogram
import subprocess
from projectshort import (
    DOWNLOAD_LOCATION
)
from projectshort.helper_funcs.display_progress import (
    progress_for_pyrogram,
    humanbytes
)




async def incoming_message_f(client, message):
    """/leech command"""
    print(message)
    i_m_sefg = await message.reply_text("checking ", quote=True)
    local_file_name = 'C:\\Users\\Buddha\\Desktop\\Python\\Publicleech\\PublicLeech-master_2\\demo.mp4'

    new_download_location = os.path.join(DOWNLOAD_LOCATION,str(time.time()))
    new_download_location = new_download_location + "/" 
        
    if not os.path.isdir(new_download_location):
        os.makedirs(new_download_location)
    print(new_download_location)
    ################# download section ###############
    try:
        url = message.reply_to_message.text
        print(url)
    except:
        url = message.reply_to_message 
        print(url,"except")   


    command =[
                    "youtube-dl",
                    "--no-warnings",
                    "--console-title",
                    "-c",
                    "--retries=10",
                    "-o"+new_download_location +"%(title)s.%(ext)s",
                    url
                ]
    process = subprocess.call(command, shell=False)
    ############## found file ########################

    if os.path.isdir(new_download_location):
        directory_contents = os.listdir(new_download_location)
        directory_contents.sort()
        # number_of_files = len(directory_contents)
        # LOGGER.info(directory_contents)
        new_m_esg = message
        
        new_m_esg = await message.reply_text(
            "Found {} files".format(len(directory_contents)),
            quote=True
        )
            
    for i in directory_contents:
        print(new_download_location + i)
        local_file_name = new_download_location + str(i) 
        
                


    ############### up;oad section ####################
        start_time = time.time()
        message_for_progress_display = await message.reply_text(
            "starting upload of {}".format(os.path.basename(local_file_name))
        )


        await message.reply_document(
            document=local_file_name,
            parse_mode="html",
            disable_notification=True,
            progress=progress_for_pyrogram,
            progress_args=(
                "trying to upload",
                message_for_progress_display,
                start_time
            )
        )
                    

                    
                    
                    
                    
                    
   
