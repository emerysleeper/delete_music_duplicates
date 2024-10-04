import os
import re
from math import floor
from mutagen.mp3 import MP3


path_to_music = '../разное'


allfiles_arr = os.listdir(path_to_music)
# allfiles = os.listdir()
# print(allfiles_arr[0])


# i = 0

for name in allfiles_arr:

#In case we dont want to delete everything, testing purposes
#     i+=1
#     if i >= 1000:
#         break


    regexp = "-[0-9]+\.mp3"


    #Check if there is ending like song-1.mp3, song-2.mp3 etc
    res = bool(re.search(regexp, name))
    #If there is, create clean name and check if length is roughly the same
    try:
        if res:
            clean_name = re.sub(regexp, ".mp3", name)

            #This is for file sizes
            #original_file_size = floor((os.stat(f'{path_to_music}/{clean_name}').st_size)/1000)
            #copied_file_size = floor((os.stat(f'{path_to_music}/{name}').st_size)/1000)


            original_file_length = floor(MP3(f'{path_to_music}/{clean_name}').info.length)
            high_point = original_file_length*1.1
            low_point = original_file_length*0.9
            copied_file_length = floor(MP3(f'{path_to_music}/{name}').info.length)

            #Check music length
            if low_point < copied_file_length < high_point:
                print(clean_name)
                print(original_file_length)
                print(copied_file_length)
                os.remove(f'{path_to_music}/{name}')

            #Check file sizes, if the copy is equal to original - delete it
#             if original_file_size == copied_file_size:
#                 print(clean_name)
#                 print(original_file_size)
#                 print(copied_file_size)
#                 os.remove(f'{path_to_music}/{name}')
    except:
        continue