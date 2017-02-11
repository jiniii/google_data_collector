import json
import webbrowser

import httplib2

from apiclient import discovery
from oauth2client import client

from google_data_collector import GoogleDataCollector

if __name__ == '__main__':
  flow = client.flow_from_clientsecrets(
    'cs',
    scope=('https://www.googleapis.com/auth/plus.login','https://www.googleapis.com/auth/plus.circles.read'),
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

  auth_uri = flow.step1_get_authorize_url()
  webbrowser.open(auth_uri)

  auth_code = input('Enter the auth code: ')

  credentials = flow.step2_exchange(auth_code)
  col = GoogleDataCollector()
  col.set_database('root','computer')
  #print(credentials.access_token)
  col.insert_user_data(credentials.access_token)


  #http_auth = credentials.authorize(httplib2.Http())

  '''
  drive_service = discovery.build('drive', 'v2', http_auth)
  files = drive_service.files().list().execute()
  for f in files['items']:
    print (f['title'])
    '''