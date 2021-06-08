from os import access
import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self,files_from,files_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,file in os.walk(files_from):

               for file_name in file:

                 localPath = os.path.join(root, file_name)
                 relative_path = os.path.relpath(localPath, files_from)
                 dropbox_path = os.path.join(files_to, relative_path)

                 with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'axhsO21OqHcAAAAAAAAAAZfDwaiTz7nGTh5HGRCsfABGQ6tVQG-zAb0oamOUnP8e'
    transferData = TransferData(access_token)

    files_from = input("Which files do you want to Upload?")
    files_to = input("Enter the Path to upload to DropBox")
    
    transferData.upload_files(files_from, files_to)
    print("File has been moved.")

main()