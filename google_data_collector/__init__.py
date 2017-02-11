"""
    Copyright (C) 2017 Jinitha Paul

    This file is part of google-data-collector.

    google-data-collector is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.https://www.googleapis.com/plus/v1/people/me
    google-data-collector is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with google-data-collector.  If not, see <http://www.gnu.org/licenses/>.
"""
import pymysql

from google_data_collector.database import database
from googledata import GoogleData


class GoogleDataCollector:

    def __init__(self):
        self.api = GoogleData()

    def set_database(self,username,password,host="localhost"):
        self.database=database(username,password,host)

    def insert_user_data(self,access_token):
        data=self.api.get_data(access_token)
        print(data)
        self.database.insert_user_data(data['id'],data['language'],data['displayName'],str(data.get('location',"")),data['gender'],data['image']["url"])





