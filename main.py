import os
import shutil

FOLDER_Path = os.getcwd()

File_Types = {
   "PDFs": [".pdf"],
    "Word_Files": [".docx", ".doc"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Text_Files": [".txt", ".html"],
     "Drawio_Files": [".drawio"]
     
}

for folder in File_Types:
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in os.listdir(FOLDER_Path):
   if os.path.isdir(file):
     continue
   ext = os.path.splitext(file)[1].lower()

   for folder, extensions in File_Types.items():
      if ext in extensions:

       shutil.move(file, os.path.join(folder, file))
       break
      
print("File organized successfully.") 


  

