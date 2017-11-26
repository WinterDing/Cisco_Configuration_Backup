#!/usr/bin/python
#coding:utf-8

import os

#File operation: read, write, append
class File_Operation(object):
    def __init__(self, path):
        self.path = path
    def file_write(self, write_content):
        with open(self.path,'w') as f:
            line = '%s\r\n' % write_content
            f.write(line)
    def file_writelines(self,write_content):
        with open(self.path,'w') as f:
            for line in write_content:
                line = '%s\r\n' % line
                f.writelines(line)
    def file_append(self, write_content):
        with open(self.path,'a') as f:
            line = '%s\r\n' % write_content
            f.write(line)
    def file_appendlines(self,write_content):
        with open(self.path,'a') as f:
            for line in write_content:
                line = '%s\r\n' % line
                f.writelines(line)

#Folder operation: create, delete
class Folder_Operation(object):
    def __init__(self, site, path, folder_date):
        self.site = site
        self.path = path
        self.folder_date = folder_date
    #create folder tree
    def folder_makedirs(self):
        self.folder_site = ''.join([self.path,self.folder_date,'\\',self.site])
        #judge if folder exists or not, if exists, then keep the old ones, this could be change
        if os.path.exists(self.folder_site):
            pass
        else:
            os.makedirs(self.folder_site)
        return self.folder_site

    def folder_makedir(self):
        pass