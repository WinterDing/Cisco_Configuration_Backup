#!/usr/bin/python
#coding:utf-8

import paramiko
from os_operation import File_Operation

def ssh_operation(device,username,password,commands,folder_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh connection succeed or fail
    device_configuration_file_path = ('%s\\%s.txt') % (folder_path,device)
    for command in commands:
        try:
            ssh.connect(device,22,username,password)
            #run commands one by one
            stdin,stdout,stderr = ssh.exec_command(command)
            #write output in screen into files
            command_print = '#%s\r\n' % command
            split_print = '\r\n%s\r\n' % ('+'*150)
            Backup_configuration = File_Operation(device_configuration_file_path)
            output = stdout.read()
            final_output = ''.join([command_print,output,split_print])
            Backup_configuration.file_append(final_output)
            mesg = '%s:  configuration backup successfully\r\n' % device.split('.')[0]
        except Exception:
            mesg = '%s:  ssh connection failed\r\n' % device.split('.')[0]
            ssh.close()
            break
    #return log message
    return mesg

def ssh_authentication(username,password):
    authtication_ssh = paramiko.SSHClient()
    authtication_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        authtication_ssh.connect('shzn40001.apa.zf-world.com',22,username,password)
    except paramiko.AuthenticationException:
        result = 'fail'
    except Exception:
        result = 'exit'
    else:
        result = 'pass'
    finally:
        return result



