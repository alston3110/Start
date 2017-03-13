# -*- coding: utf8 -*-
import os
import sys
import platform
import socket
import fcntl
import struct
import array
#import netifaces
#import netaddr
import commands

# ----------------------------------------------------------------------
# CPU & System Base Information
def Get_OSType() :
    # 'posix', 'nt', 'os2', 'ce', 'java', 'riscos'
    return os.name 

def Get_Platform() :
    # Linux (2.x and 3.x)	'linux2'
    # Windows				'win32'
    # Windows/Cygwin		'cygwin'
    # Mac OS X				'darwin'
    # OS/2					'os2'
    # OS/2 EMX				'os2emx'
    # RiscOS				'riscos'
    # AtheOS				'atheos'
    return sys.platform

def Get_CPUNumber() :
    return commands.getoutput("grep -c processor /proc/cpuinfo")

# ----------------------------------------------------------------------
# Network Information
def Get_HostName() :
    return socket.gethostname()

def Get_HwAddr(ifname) :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

def Get_IPAddress(ifname) :
    addrs = netifaces.ifaddresses(ifname)
    return addrs[socket.AF_INET][0]

def Get_Interfaces() :
    return netifaces.interfaces()


class Obj:
    def __init__ (self):
        self.Data = {}
        self.Data['hostname'] = Get_HostName()
        self.Data['mac'] = Get_HwAddr('eth0')
        self.Data['if0'] = Get_IPAddress('eth0')
        self.Data['if1'] = Get_IPAddress('lo')
        print self.Data['hostname']
        print self.Data['mac']
        print self.Data['if0']['addr']
        print self.Data['if0']['addr']
        print self.Data['if1']['netmask']
        print self.Data['if1']['netmask']

        
