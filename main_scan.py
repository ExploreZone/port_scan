#coding:utf-8

import optparse
import socket
from socket import *






#portScan函数

def portScan(tgthost,tgtports):
    try:
        tgtIP = gethostbyname(tgthost)

    except Exception as e:
        print "[-] cannot resolve '%s': Unknow host"%(tgthsot)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Result for :'+tgtName[0]
    except Exception as e:
        print '\n[+] Scan Result for :'+tgtIP
    setdefaulttimeout(1)
    for tgtport in tgtports:
        print "Scan port:"+tgtport
        connScan(tgthost,int(tgtport))
def connScan(tgthost,tgtport):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgthost,tgtport))
        connSkt.send('ViolenPython\r\n')
        result = connSkt.recv(100)
        print '[+]%d/ tcp open'%(tgtport)
        if str(result):
            print '[%d banner]'%(tgtport)+str(result)
            connSkt.close
    except Exception as e:
        print '[-]%dtcp closed'%(tgtport)
        #main函数
def main():
    parser = optparse.OptionParser('usage%prog'+'-H -p')

    parser.add_option('-H',dest='tgthost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtports',type='string',help='specify target port[s] by tools')
    (options,args)=parser.parse_args()

    tgthost = options.tgthost

    tgtports = str(options.tgtports).split(',')
    if (tgthost==None) | (tgtports[0] ==None):
        print '[-] You must specify a target host and port[s].'
        print parser.usage
        exit(0)
    #执行portScan函数
    portScan(tgthost,tgtports)
if __name__ == '__main__':
    main()

