Script is using JSON file to keep data between executions.

Dependencies:

Script is depended to scapy. Please install it by 

> pip install scapy


The script use list variable to store ports which need to be scanned (this is just workarround to speed up the proces of scanning.) The next step to enpover the script can be put whole portrange [1-65535] and use Threads to paralelize the execution. 
