import os
import  csv
import string

def WriteLine(USER,NTNAME,AUTHID):
    file_name = 'Access.txt'
    auth_mode= 'r+'
    data_list =[]
    with open(file_name,auth_mode) as file:
        for eachline in file:
            x = [(eachline).rstrip('\n')]
            data_list.append(x)
        length_file = len(data_list)
        data_send = USER+NTNAME+AUTHID
        print(data_send)
        for rowindex in range(0,length_file):
            if data_send == "".join(data_list[rowindex]):
                break
            else:
                file.write(USER+','+NTNAME+','+AUTHID)
                print("".join(data_list[rowindex]))




x = WriteLine('NAME','HGHHG','JHJJ')