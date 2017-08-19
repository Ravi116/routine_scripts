# routine_scripts

Its collection of scripts which automates daily task.

1. Autossh
	it creates expect script to take remote ssh of given server info.
		and moves that script to /usr/sbin/ so it can be directly used from anywhere as commnad.
	dependencies:
			you must install expect package to ssh script to work.
			
			command: apt install expect or yum install expect
			
			note: if you face issue related to expect not found or somthing like that try it after a restart of your system.
 
usage : autossh server_name IPaddress username(optional) port(optional)
	autossh demo_server xxx.xxx.xxx.xxx
		
	if username is diffrent than root
		autossh demo_server xxx.xxx.xxx.xxx  demo_user
	if port is diffrent 
		autossh demo_server xxx.xxx.xxx.xxx root port_no

2.multitab
			


