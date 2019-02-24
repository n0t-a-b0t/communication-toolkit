# COMMUNICATION TOOLKIT

Chat, File search and File transfer utility.

### chatbox.py

Basic point-to-point chat utility through CLI.

Usage:
```
python chatbox.py [mode] [host] [port]
mode:
-fs : Act as server
-fc : Act as client
host: Server IPv4 Address
port: Server port number
```

### chatbox_broadcast.py

Broadcast server for group chat utility through CLI.

Usage:
```
python chatbox_broadcast.py [host] [port]
host: Server IPv4 address
port: Server port number

Note: All group chat clients should run chatbox.py in client mode
```

### file_search.py

Searches specified file in local or foreign system.

Usage:
```
For local file search:
  python file_search.py -l [filename]
 
 For foreign file search:
  System initiating the search should run as client...
  python file_search.py -fc [filename] [host] [port]
  host: Server IPv4 Address
  port: Server port number
 
  System on which file will be searched should be run as server...
  python file_search.py -fs [host] [port]
  host: Server IPv4 Address
  port: Server port number
  
NOTE: Windows users should enter path with double-slashes
E.g: "C:\Users\Documents" should be entered as "C:\\Users\\Documents"
```

### file_transfer_server.py

Server for file transfer operations. Files will be downloaded from or uploaded to the server machine.

Usage:
```
python file_transfer_server.py [host] [port]
host: Server IPv4 Address
port: Server port number
```

### file_transfer_client.py

Client for file transfer operations. Files will be downloaded to or uploaded from the client system.

Usage:
```
python file_transfer_client.py [mode] [filename] [host] [port]

mode:
-d: download
-u: upload

filename: File name (with path if needed) to be downloaded or uploaded.

NOTE: Files can be downloaded from various server directories if you give the right path, but will be uploaded to the server's hosting directory only; as in the directory from which the file_transfer_server.py is running from.

NOTE: Windows users should use double-slashes in the path.
E.g: "C:\Users\Documents" should be entered as "C:\\Users\\Documents"

host: Server IPv4 Address
port: Server port number
```

### cover.py

Program to run the above programs in an easy/understandable manner.

Usage:
```
python cover.py
```
