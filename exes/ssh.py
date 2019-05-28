#!/usr/bin/python3


import sys
import paramiko
from optparse import OptionParser

exitstatus = 1

usage = "USAGE: %prog [options]"

parser = OptionParser(usage=usage)

parser.add_option("--host",metavar="HOSTNAME", help = 'Hostname for SSH command')

parser.add_option("-u","--username",metavar="USERNAME", help = 'Username for SSH command')

parser.add_option("-p","--password", metavar="PASSWORD", help="Password for SSH command" )

parser.add_option("-c", "--command", metavar="COMMAND", help="command to run")

options, args = parser.parse_args()

print(options.num)

print(args)
if len(args) != 0:
    parser.error("Only Options are ")
    sys.exit(exitstatus)

hostname = options.host
username = options.username
password = options.password
command = options.command
port=22

try:
    
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    print("creating SSH connection . . . ")

    client.connect(hostname,port=port, username=username, password=password)
    
    print("connected to "+hostname)
    
    print("command to execut: "+command)

    stdin, stdout, stderr = client.exec_command(command)

    print("----Output START----")
    for line in stdout:
        print(line.rstrip())
    
    print("---- Output END----")
    exitstatus= 0
 
except Exception as e:

    print("ERROR:",e)

finally:
    print("closing connection . . . ")
    client.close()
    print("Exit Status = "+ str(exitstatus))
    sys.exit(exitstatus)
