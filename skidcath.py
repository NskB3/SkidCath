#!/usr/bin/env python2
#encoding=utf8
######################
#    RUN AS ROOT.    #
######################
__author__ = "XynMaps/XantiSec/Dump"

import socket
import sys
import threading
import time

try:
	import colors
except:
	print("[-] Colors module not found, ask %s for it!" % __author__)
	quit()
def platform_check():
	platform = sys.platform
	if "x" not in platform:
		print(colors.red + "This is only for Linux/Unix systems, sorry!")
		quit()
	else:
		print(colors.green + "[+] Platform check done!")
def server(port):
	logfile = "/etc/SkidCath_LOG.log"
	s = socket.socket()
	print(colors.yellow)
	#print("Attempting to bind socket...")
	time.sleep(0.5)
	try:
		s.bind(("", port))
	except Exception as e:
		print(colors.red + "[-] Failed to bind socket, due to:" + str(e) +colors.end)
		quit()
	#print(colors.green + "[+] Socket binded successfully!")
	#print(colors.yellow + "Attempting to set up listener...")
	time.sleep(0.5)
	try:
		s.listen(10)
	except Exception as e:
		print(colors.red + "[-] Failed to set up listener, due to:" + str(e) + colors.end)
                quit()
	#print(colors.green + "[+] Listener setup done!")
	#print(colors.yellow + "Server runnning, waiting for connections..." + colors.end)
	while 1:
		try:
			conn, addr = s.accept()
			if addr[0] != "127.0.0.1":
				print(colors.green + "[LOGGED] {}".format(addr[0]))
				open(logfile, "a").write(str(addr).split(",")[0].replace('(', '').replace(')', '').replace("'", "") + "\n")
				reply = "Hey skid. You have been caught by SkidCath. You are a disgrace to humanity, bye."
				conn.send(reply)
				conn.close()
		except: pass
if __name__ == '__main__':
	print(colors.dark_yellow  + """
|__;-----------------;__|
|__; Dump's SkidCath ;__|
|__;-----------------;__|
""")
	platform_check()
	ports = [22, 23, 37215, 53413, 8083, 49152]
	for port in ports:
		threading.Thread(target=server, args=(port,)).start()
	print(colors.yellow + "Server runnning, waiting for connections..." + colors.end)
