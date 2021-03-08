import asyncio
import os
import time
import pyrogram
import subprocess
from projectshort import (
    DOWNLOAD_LOCATION
)
from projectshort.unzip_file import create_unzip
from projectshort.helper_funcs.display_progress import (
    progress_for_pyrogram,
    humanbytes
)


async def upload_to_tg(
    message,
    local_file_name,
    from_user
    
):
    
    base_file_name = os.path.basename(local_file_name)
    caption_str = ""
    caption_str += base_file_name 
   
   
    if os.path.isdir(local_file_name):
        directory_contents = os.listdir(local_file_name)
              
        directory_contents.sort()
        
        #LOGGER.info(directory_contents)
        new_m_esg = await message.reply_text(
            "Found {} files".format(len(directory_contents)),
            quote=True
            
        )
        
        for single_file in directory_contents:
            
            await upload_to_tg(
                new_m_esg,
                os.path.join(local_file_name, single_file),
                from_user
               
            )
    else:
        start_time = time.time()
        message_for_progress_display = await message.reply_text(
            "starting upload of {}".format(os.path.basename(local_file_name))
        )

        caption = os.path.basename(local_file_name)
        await message.reply_document(
            document=local_file_name,
            parse_mode="html",
            disable_notification=True,
            caption = caption,
            progress=progress_for_pyrogram,
            progress_args=(
                "trying to upload",
                message_for_progress_display,
                start_time
            )
        )
        try:
            os.remove(local_file_name) 
            await message_for_progress_display.delete()
        except:
            pass
            
