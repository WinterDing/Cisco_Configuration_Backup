#!/usr/bin/python
#coding:utf-8

import parameters,devices_operations
from os_operation import File_Operation,Folder_Operation
import time
import datetime
import threading
import time

def site_ssh(site,path,folder_date,ssh_username,ssh_password):
    #crete folder to store backup configuration
    site_folder = Folder_Operation(site,path,folder_date)
    site_folder_path = site_folder.folder_makedirs()
    #create log file for this site
    site_log = []
    #record backup time in site log
    backup_time = time.strftime('%Y-%m-%d %H:%M:%S')
    site_log.append('Backup time: %s' % (backup_time))
    #loop all switches in this site
    for member in range(40001,40051):
        #create full name of switches
        switch_full_name = '{0}n{1}.apa.zf-world.com'.format(str(site),str(member))
        #opertate this switch
        site_mesg = devices_operations.ssh_operation(switch_full_name,ssh_username,ssh_password, \
                                                     parameters.ssh_commands,site_folder_path)
        site_log.append(site_mesg)
    #create log file and write logs into file
    site_log_file_path = '{0}\\{1}_log.txt'.format(str(site_folder_path),str(site))
    site_log_file = File_Operation(site_log_file_path)
    site_log_file.file_writelines(site_log)


def main():
    #print welcome message
    parameters.banner()
    #get path you want to operate
    path = parameters.path
    #get sites and sites switches list you want to backup
    operation_sites = parameters.switches()
    #username and password authentication verfification
    flag = 'fail'
    while (flag == 'fail'):
        #Require username and password
        ssh_username, ssh_password = parameters.username_password()
        result = devices_operations.ssh_authentication(ssh_username,ssh_password)
        #authentication fail
        if result == 'fail':
            print 'Your username or password is wrong, please input again: '
        elif result == 'exit':
            print 'shzn40001 ssh connection fail, please check shzn40001 ssh connection '\
                   'or use another switch to do authentication verification, program will exit'
            exit()
        #authentication pass
        elif result == 'pass':
            print 'Username and password are correct'
            flag = 'pass'

    print 'Start to backup switch configuration, please wait...'

    folder_date = str(datetime.date.today()).replace('-','_')
    threading_list = []

    for site in operation_sites:
        ssh_threading = threading.Thread(target=site_ssh,args=(site,path,folder_date,ssh_username,ssh_password))
        ssh_threading.start()
        threading_list.append(ssh_threading)
    for threading_member in threading_list:
        threading_member.join()
        '''
        #crete folder to store backup configuration
        site_folder = Folder_Operation(site,path,folder_date)
        site_folder_path = site_folder.folder_makedirs()
        #create log file for this site
        site_log = []
        #record backup time in site log
        backup_time = time.strftime('%Y-%m-%d %H:%M:%S')
        site_log.append('Backup time: %s' % (backup_time))
        #loop all switches in this site
        for member in range(40001,40050):
            #create full name of switches
            switch_full_name = '%sn%s.apa.zf-world.com' % (site,member)
            #opertate this switch
            site_mesg = devices_operations.ssh_operation(switch_full_name,ssh_username,ssh_password,\
                                             parameters.ssh_commands,site_folder_path)
            site_log.append(site_mesg)
        #create log file and write logs into file
        site_log_file_path = '%s\\%s_log.txt' % (site_folder_path,site)
        site_log_file = File_Operation(site_log_file_path)
        site_log_file.file_writelines(site_log)
        '''
    print 'Task done, please go to check log file and configuration backup files in %s\\%s' % (path,folder_date)
    while True:
        end_mesg = raw_input('please input "y" to stop the program: ')
        if end_mesg == 'y':
            break

if __name__ == '__main__':
    main()