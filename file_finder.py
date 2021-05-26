#importing the os module for the directory checking
import os
from match import res_perc

target = input("Name of the file you are looking for: ")
print("What is the type of the file?\n1.Text\n2.Video\n3.Audio\n4.Readme\n5.Any")
file_type = input("(1/2/3/4/5)?: ")
#path = input("Directory to look in: ")

extensions = {
    "1": "txt",
    "2": "mp4",
    "3": "mp3",
    "4": "md",
    }

if file_type != '5':
    extended_name = target + f".{extensions[file_type]}"

else:
    extended_name = target
print(extended_name)

result = []
def search(file_name):
    print("This may take some time.")
    #removed the dirs because it is not used in this case
    for root,_, files in os.walk(r"C:\\"):
        for file in files:
            if file == file_name or extended_name == file:
                print(rf'[INFO]Go to: {root}\{str(file)}')
                result.append(rf"{root}\{str(file)}")
            #similarity depending on the percentage of the match.py module and if the two files' names are the same    
            elif res_perc(list(file_name), list(file))>=50.0 and (list(file)[0] == list(file)[0]):
                print(rf'[INFO]Similar file at: {root}\{str(file)}')
                result.append(rf"{root}\{str(file)}")
            else:
                pass

    if len(result) == 0:
        print("No file matched.")

search(target)
