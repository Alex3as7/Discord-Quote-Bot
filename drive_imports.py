import os
import io
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service

def download():
    file_ids = ['10TQ4UIejx356bss7uioOdwQQqkqmT2C7']
    file_names = ['quote_book.txt']
    client_secret = 'client_secret.json'
    api_name = 'drive'
    api_version = 'v3'
    scopes = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(client_secret,api_name,api_version,scopes)

    for file_id,file_name in zip(file_ids,file_names):

        request = service.files().get_media(fileId=file_id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd = fh , request=request)

        done = False
    
        while not done:
            status,done = downloader.next_chunk()
            print('Download Prograss {0}'.format(status.progress() * 100))
        fh.seek(0)

        with open(os.path.join('',file_name),'wb') as f:
            f.write(fh.read())
            f.close()


