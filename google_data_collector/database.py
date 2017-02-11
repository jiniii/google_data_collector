import pymysql

class database:


    def __init__(self,username,password,host="localhost"):

        self.username = username
        self.password = password

        db = pymysql.connect(host='localhost', user=username, password=password, use_unicode=True, charset="utf8")
        cur = db.cursor()

        sql = 'CREATE DATABASE  IF NOT EXISTS GOOGLE_DATA'
        cur.execute(sql)

        sql = 'USE GOOGLE_DATA'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS USER(ID CHAR(200) PRIMARY KEY ,' \
              'LANGUAGE CHAR(15) ,'\
              'DISPLAYNAME CHAR(25) NOT NULL,' \
              'LOCATION CHAR(25) ,'\
              'GENDER CHAR(10) NOT NULL,'\
              'IMAGE MEDIUMTEXT NOT NULL )'
        cur.execute(sql)
        '''
        sql = 'CREATE TABLE IF NOT EXISTS CIRCLE(CID NUMERIC(50) PRIMARY KEY,' \
              'CNAME CHAR(25) NOT NULL)'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS PAGES(PID NUMERIC(50) PRIMARY KEY,' \
              'PNAME CHAR(25) NOT NULL)'
        cur.execute(sql)


        sql = 'CREATE TABLE IF NOT EXISTS PEOPLE(LID NUMERIC(50) PRIMARY KEY,' \
              'LNAME CHAR(25) NOT NULL)'
        cur.execute(sql)
    '''
    def insert_user_data(self,id, language, name,location,gender,image):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE GOOGLE_DATA'
        cur.execute(sql)
        sql = "INSERT INTO USER(ID,DISPLAYNAME,LOCATION,LANGUAGE,GENDER,IMAGE) VALUES(" + str(
            id) + ",'" + str(name) + "','" + str(location) + "','" + str(language) + "','" + str(gender) + "','"+image+"')"
        cur.execute(sql)
        db.commit()
    '''
    def circle_data(self, id, cid, cname):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE GOOGLE_DATA'
        cur.execute(sql)
        sql = "INSERT INTO CIRCLE(CID,CNAME) VALUES(" + str(cid) + ",'" + cname + "')"
        cur.execute(sql)
        db.commit()

    def pages_data(self, pid, pname):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE GOOGLE_DATA'
        cur.execute(sql)
        sql = "INSERT INTO PAGES(PID,PNAME) VALUES(" + str(pid) + ",'" + pname + "')"
        cur.execute(sql)
        db.commit()

    def people_data(self, lid, lname):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE GOOGLE_DATA'
        cur.execute(sql)
        sql = "INSERT INTO PEOPLE(LID,LNAME) VALUES(" + str(lid) + ",'" + lname + "')"
        cur.execute(sql)
        db.commit()
    '''