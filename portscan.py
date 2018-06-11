# coding:utf-8

import socket
import optparse
from sccket import *
from optparse import OptionParser

def portscan(tghost,tgports):
    tgIP = gethostbyname(tghost)
    tgname = gethostbyaddr(tgIP)
    for tgport in tgports:
        connport(tghost,tgport)
def connport(tghost,tgport):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(tghsot,tgport)


def main():
    usage = 'usage: %prog [options] arg1 arg2 ...'
    parser = OptionParser(usage, version='%prog 1.0')
    parser.add_option("-h",help="your target host ip", type="string", dest="tghost")
    parser.add_option("-p",help="your target host port", type="string", dest="tgport")
    (options, args) = parser.parse_args()
    tghost = options.tghost
    tgports = options.tgport.sploit(',')
    portscan(tghost,tgports)
if __name__ == '__main__':
    main()