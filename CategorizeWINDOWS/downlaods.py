import os

source_folder = r'D:\Downloads' + '//'
base_target_folder = r'D:\Downloads' + '//'
videos = r'D:\Downloads\Video' + '//'
music = r'D:\Downloads\Music' + '//'
images = r'D:\Downloads\Images' + '//'
docs = r'D:\Downloads\Documents' + '//'
exe = r'D:\Downloads\Programs' + '//'
zip = r'D:\Downloads\Compressed' + '//'
other = r'D:\Downloads\Other' + '//'



def move_files(source_folder , base_target_folder):
    try:
        for path , dirs , files in os.walk(source_folder):
            # path = r'D:\Downloads' + '//'
            # print('Searching:', path)
            # print('All directories', dirs)
            # print('All files:', files)
            # print('----------------------')
            if files :
                for file in files:
                    s1 = file[-3:]
                    if s1 in ["mkv" , "mp4"]:
                        base_target_folder = videos
                    elif s1 in ["mp3" , "m4a"]:
                        base_target_folder = music
                    elif s1 in ["jpg" , "png" , "peg" , "fif" ]:
                        base_target_folder = images
                    elif s1 in ["txt" , "pdf" , "ocx" , "pub" , "htm" ,"ptx" , "xml" , "php" , "lsx" ,"ics"]:
                        base_target_folder = docs
                    elif s1 in ["zip" , "rar"]:
                        base_target_folder = zip
                    elif s1 in ["exe" , "jar" , "msi" , "appinstaller"]:
                        base_target_folder = exe
                    else:
                         base_target_folder = other
                        
                    if not os.path.isfile(base_target_folder + file):  # if this file from this folder does not exists in target folder , then move it 
                        os.rename(path + '//' + file , base_target_folder + file)
        print('All Files moved')

    except Exception as e:
        print(e);    

move_files(source_folder , base_target_folder)

#print(target_folder)
#print(source_folder)








