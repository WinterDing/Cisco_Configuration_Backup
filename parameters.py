#!/usr/bin/python
#coding:utf-8

#path you want to put files in
path = r'\\path'
#ssh commands want to run on devices
ssh_commands = ['show run','show vlan brief',\
                'show ip interface brief',\
                'show cdp neighbors',\
                'show etherchannel summary',\
                'show version']
#ssh_commands = ['show run','show vlan brief']

#Require user for username and password
def username_password():
    username = raw_input('please input username: ')
    password = raw_input('please input password: ')
    return (username,password)

#Ask user which sites' switches do you want to operate
def switches():
    #all apa sites code
    apa_sites = ['xxx','xxx']
    #all sites or specific site
    while True:
        choice = raw_input("Which location's switches do you want to operate (all or specific site): ")
        #all apa sites
        if choice == 'all':
            operation_sites = apa_sites
            break
        #one site
        elif choice in apa_sites:
            operation_sites = choice.split()
            break
        #site name is not in apa sites list
        else:
            print 'This site is not in site_lists, please enter site name again'
    #return sites and switches
    return operation_sites
#banner
def banner():
    welcome_mesg = 'Welcome to network devices management system'
    description_mesg = 'The system is used to backup configuration of all apa switches'
    banner_mesg = ['+'.join(['', '-' * 78, '']), welcome_mesg.center(80), description_mesg.center(80),
                   '+'.join(['', '-' * 78, ''])]
    for mesg in banner_mesg:
        print mesg

