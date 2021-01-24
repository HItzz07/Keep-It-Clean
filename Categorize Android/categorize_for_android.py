import os

source_folder = r'/data/data/com.termux/files/home/storage/shared/Download' + '//'
base_target_folder = r'/data/data/com.termux/files/home/storage/shared/Download' + '//'
videos = r'/data/data/com.termux/files/home/storage/shared/Download/Videos' + '//'
music = r'/data/data/com.termux/files/home/storage/shared/Download/Music' + '//'
images = r'/data/data/com.termux/files/home/storage/shared/Download/Images' + '//'
docs = r'/data/data/com.termux/files/home/storage/shared/Download/Docs' + '//'
apks = r'/data/data/com.termux/files/home/storage/shared/Download/Apks' + '//'
zip = r'/data/data/com.termux/files/home/storage/shared/Download/Zip' + '//'



def move_files(source_folder , base_target_folder):
    try:
        for path , dir , files in os.walk(source_folder):
            if files:
                for file in files:
                    s1 = file[-3:]
                    if s1 in ["mkv" , "mp4"]:
                        base_target_folder = videos
                    elif s1 in ["mp3"]:
                        base_target_folder = music
                    elif s1 in ["jpg" , "png"]:
                        base_target_folder = images
                    elif s1 in ["txt" , "pdf" , "ocx" , "pub" ]:
                        base_target_folder = docs
                    elif s1 in ["zip"]:
                        base_target_folder = zip
                    elif s1 in ["apk"]:
                        base_target_folder = apks
                        
                    if not os.path.isfile(base_target_folder + file):  # if this file from this folder does not exists in target folder , then move it 
                        os.rename(path + '//' + file , base_target_folder + file)
        print('All Files moved')

    except Exception as e:
        print(e);    

move_files(source_folder , base_target_folder)

#print(target_folder)
#print(source_folder)








