import os
import string
import csv



class CreateUser:
    def __init__(self,USER,NTNAME,ACCOUNTID):
        self.USER= USER
        self.NTNAME = NTNAME
        self.ACCOUNTID = ACCOUNTID


    def CreateFile(self):
           credential="".join(list(self.USER+','+self.NTNAME+','+self.ACCOUNTID))
           file_name = 'Access.txt'
           auth_type = 'r+'
           with open(file_name, auth_type) as f:
               if name not in f:
                   f.write(name)
               else:
                   pass


user2 = CreateUser('dgfd','gdf','jh')
user2.CreateFile()





