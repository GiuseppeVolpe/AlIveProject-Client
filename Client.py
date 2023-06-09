# Import socket module
import socket
import pickle
import time

def Main():
	# local host IP '127.0.0.1'
    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 12345
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))
    
    time.sleep(2)
	
    user = "GiuseppeVolpe"
    model = "NerModel_bert2"

    while True:
        
        sentence = input("Type something to predict: ")

        alive_request = {
            "user" : user,
            "model" : model,
            "sentence" : sentence
        }
        
        s.send(pickle.dumps(alive_request))

        # message received from server
        data = s.recv(1024)
        response = pickle.loads(data)

        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', response)

        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')

        if ans == 'y':
            continue
        else:
            break
        
    # close the connection
    s.close()

if __name__ == '__main__':
	Main()
