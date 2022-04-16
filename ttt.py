import urllib.parse
import urllib.request
import os, sys
import ssl
import ftplib

host = 'chizhtopl.ru'
ftp_user = 'cacady@chizhtopl.ru'
ftp_password = 'Tramadol1989'
ftp = ftplib.FTP(host, ftp_user, ftp_password)
dd = ftp.nlst()
print(dd)