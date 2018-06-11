
#-*-coding:utf-8-*-

import optparse

import socket

from socket import *

def connScan(tgthost,tgtport):

   try:                    #尝试去建立端口的连接并发送垃圾数据

       connSkt=socket(AF_INET,SOCK_STREAM)

       connSkt.connect((tgthost,tgtport))

       connSkt.send('ViolenPython\r\n')

       result=connSkt.recv(100)

       print '[+]%d/tcp open'%(tgtport)    #如果没有出错，打印端口开放，并把接收到的banner信息打印出来

       if str(result):

           print '[ %d banner]'%(tgtport)+str(result)

       connSkt.close()

   except:                             #如果出错，则打印端口关闭

       print '[-]%d/tcp closed'%(tgtport)

def portScan(tgthost,tgtports):

   try:

       tgtIP=gethostbyname(tgthost)

   except:

       print "[-] Cannot resolve '%s': Unknow host"%(tgthost)

       return

   try:

       tgtName=gethostbyaddr(tgtIP)

       print '\n[+] Scan Result for:'+tgtName[0]

   except:

       print '\n[+] Scan Result for:'+tgtIP

   setdefaulttimeout(1)

   for tgtport in tgtports:

       # print 'Scanning port '+tgtport

       connScan(tgthost,int(tgtport))

def main():

   parser=optparse.OptionParser('usage%prog'+'-H <target host> -p <target port>')

   parser.add_option('-H',dest='tgthost',type='string',help='specify target host')

   parser.add_option('-p',dest='tgtport',type='string',help='specify target port[s] by comma')

   (options,args)=parser.parse_args()

   tgthost=options.tgthost

   tgtports=str(options.tgtport).split(',')

   if (tgthost == None) | (tgtports[0] == None): #判断是否有ip和端口参数，没有则输出帮助信息并退出

       print '[-] You must specify a target host and port[s].'

       print parser.usage

       exit(0)

   portScan(tgthost,tgtports)   #跳到portScan()函数

if __name__ == '__main__':

   main()