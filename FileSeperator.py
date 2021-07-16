import os,shutil

dict_extension = {
'audio_Ext' : ('.mp3','.m4a','.wav','.flac'),
'video_Ext' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
'Doc_Ext' : ('.docx','.pdf','.txt')
}




folderPath = input('Enter folder path')

def File_finder(folder_path,file_extensn):
    files = []
    for file in os.listdir(folder_path):
        for ext in file_extensn:
            if file.endswith(ext):
                files.append(file)
    return files

#print(File_finder(folderPath,video_Ext))

for extension_type,extension_tuple in dict_extension.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderPath,folder_name)
    os.mkdir(folder_path)
    for item in File_finder(folderPath,extension_tuple):
        item_path = os.path.join(folderPath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
        


