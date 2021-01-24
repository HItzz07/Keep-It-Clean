import os

source_folder = r'This PC\Mi A1\Internal shared storage\Download' + '\\'
def move_files(source_folder , base_target_folder):
    try:
        for path , dir , files in os.walk(source_folder):
            if files:
                for file in files:
                    print(file)    
                    #if not os.path.isfile(base_target_folder + file):  # if this file from this folder does not exists in target folder , then move it 
                    #    os.rename(path + '\\' + file , base_target_folder + file)
        print('All Files moved')

    except Exception as e:
        print(e);    










