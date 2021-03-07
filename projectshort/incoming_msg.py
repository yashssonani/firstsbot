import asyncio
import os
import time
import pyrogram
import subprocess
from projectshort import (
    DOWNLOAD_LOCATION
)
from projectshort.unzip_file import create_unzip
from projectshort.upload_to_tg import upload_to_tg
from projectshort.helper_funcs.display_progress import (
    progress_for_pyrogram,
    humanbytes
)




async def incoming_message_f(client, message):
    """/leech command"""
    print(message)
    
    is_unzip = False
    
    if len(message.command) > 1:
        if message.command[1] == "unzip":
            is_unzip = True
    current_user = message.from_user.id        
    if not message.reply_to_message:
      i_m_sefg = await message.reply_text("No link or No File Found", quote=True)
      
    
            
        
        
    i_m_sefg1 = await message.reply_text("processing", quote=True)
    i_m_sefg = await message.reply_text("checking ", quote=True)
   

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
    try:
        i_m_sefg = await i_m_sefg.edit_text("trying to download")
    except:
        
        pass

    command =[
                    "youtube-dl",
                    "--no-warnings",
                    "--console-title",
                    "-c",
                    "--retries=10",
                    "-o"+new_download_location +"%(title)s.%(ext)s",
                    url
                ]
    #process = subprocess.call(command, shell=False)
    process = subprocess.Popen(command, shell=False)
    process.wait()
    ############## found file ########################
    
    if is_unzip:
        a = os.listdir(new_download_location)
        b = a[0]
        new_download_location = new_download_location + b
        new_download_location = await create_unzip(new_download_location)
        to_upload_file = new_download_location
        response = {}
        user_id = current_user
        sent_message_to_update_tg_p = i_m_sefg1
        await upload_to_tg(sent_message_to_update_tg_p,to_upload_file,user_id)
        
    else:
        to_upload_file = new_download_location
        response = {}
        user_id = current_user
        sent_message_to_update_tg_p = i_m_sefg1
        await upload_to_tg(sent_message_to_update_tg_p,to_upload_file,user_id)
    
                 

                
                    
                    
                    
                    
   
