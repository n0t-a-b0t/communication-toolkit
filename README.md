# communication_toolkit
This toolkit contains basic point-to-point and group chat, file search and file transfer capabilities that can be executed at CLI. 

Note: Python Environment: 2.7.15
These files can be executed individually or through cover.py, which will baby feed the users with the command line arguments each code takes.

Basic gist:-
chatbox.py: Point-to-Point chat program
  usage: As server- $python chatbox.py -fs <server ip> <port#>
         As client- $python chatbox.py -fc <server ip> <port#>

chatbox_broadcast.py: Sets up a server for group chats. All clients must connect to this server with the '-fc' argument
  usage: $python chatbox_broadcast.py <server ip> <port#>
  
file_search.py: Performs a file search on local as well as foreign drives (default drives: Linux: '/', Windows: 'C:\')
  usage: For local drives- $python file_search.py -l <file_name>
         For foreign drives as a server (file will be searched in your system)- $python file_search.py -fs <server ip> <port#>
         For foreign drives as a client (file will be searched in foreign system)-
                $python file_seaarch.py -fc <file_name> <server ip> <port#>

file_transfer.py: Transfers files over the network
  usage: As a server (file will be downloaded from you)- $python file_transfer.py -fs <server ip> <port#>
         As a client (file will be requested by you)- 
          $python file_transfer.py -fc <file_name to be downloaded> <file_name to be stored> <server ip> <port#>
