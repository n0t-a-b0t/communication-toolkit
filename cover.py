try:
    import easygui
except:
    print 'Switching to CLI'
import os


def f_xfer():
    print "\nThis will transfer files across the network\n"
    host = str(raw_input("\nEnter server IP: "))
    port = int(raw_input("\nEnter server port number: "))
    role = str(raw_input("\nEnter '-fs' for acting as server, '-fc' for acting as client\nEnter your choice: "))
    if role == '-fs':
        os.system('python file_transfer_server.py '+host+' '+str(port))
    elif role == '-fc':
        operation = str(raw_input("\nEnter '-d' for downloading files | '-u' for uploading files: "))
        file_path = str(raw_input("\nEnter the file path for downloading/uploading: "))
        os.system('python file_transfer_client.py '+operation+' '+file_path+' '+host+' '+str(port))
    else:
        print "\nEnter either '-fs' or '-fc' please...\n"
        f_xfer()
    return


def fsearch():
    print "\nThis will search for a file on local or foreign system\n"
    role = str(raw_input("\nEnter '-l' for local file search\nEnter '-fs' for addressing a foreign search "
                         "query\nEnter '-fc' for requesting a foreign search query\nEnter choice: "))
    if role == '-l':
        file_name = str(raw_input("\nEnter search query: "))
        os.system('python file_search.py '+role+' '+file_name)
    elif role == '-fs':
        host = str(raw_input("\nEnter IPv4 address of Server: "))
        port = int(raw_input("\nEnter server port number: "))
        os.system('python file_search.py '+role+' '+host+' '+str(port))
    elif role == '-fc':
        file_name = str(raw_input("\nEnter search query: "))
        host = str(raw_input("\nEnter IPv4 address of Server: "))
        port = int(raw_input("\nEnter server port number: "))
        os.system('python file_search.py '+role+' '+file_name+' '+host+' '+str(port))
    else:
        print "\nEnter '-l', '-fs' or '-fc' please...\n"
    return


def chat_serv():
    print "\nThis will start a group chat server\n"
    host = str(raw_input("Enter IPv4 address of server: "))
    port = int(raw_input("Enter server port number: "))
    os.system('python chatbox_broadcast.py '+host+' '+str(port))
    return


def chatops():
    print "\nThis will start a chat window with an individual client\n"
    role = str(raw_input('\nDo you want to be server or client?\nEnter -fs for server, -fc for client: '))
    print role
    if (role == '-fs') or (role == '-fc'):
        host = str(raw_input("\nEnter IPv4 address of server: "))
        port = int(raw_input("\nEnter server port number: "))
        os.system('python chatbox.py '+role+' '+host+' '+str(port))
    else:
        print "Enter either -fs or -fc"
        chatops()
    return


def handle_opt(opt):
    if opt == 'Individual Chat':
        chatops()
    elif opt == 'Host a Group Chat Server':
        chat_serv()
    elif opt == 'File Search':
        fsearch()
    elif opt == 'File Transfer':
        f_xfer()
    else:
        print "Bad Input!"
    return


def main():
    try:
        opt = easygui.buttonbox('What do you wish to do?', 'Tasking...', ('Individual Chat', 'Host a Group Chat Server', 'File Search', 'File Transfer', 'Exit'))
    except:
        opt = str(raw_input("What do you wish to do?\nIndividual Chat\nHost a Group Chat Server\nFile Search\nFile "
                            "Transfer\nExit\n\nEnter choice: "))
    if opt == 'Exit':
        return
    else:
        handle_opt(opt)
    return


main()
