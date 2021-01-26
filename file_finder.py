#importing the os module for the directory checking
import os

target = input("Name of the file you are looking for: ")
#path = input("Directory to look in: ")


result = []
def search(file_name):
    print("This may take some time.")
    #removed the dirs because it is not used in this case
    for root,_, files in os.walk(r"C:\\"):
        for file in files:
            if file == file_name:
                print(rf'[INFO]Go to: {root}\{str(file)}')
                result.append(rf"{root}\{str(file)}")

    if len(result) == 0:
        print("No file matched.")

search(target)
