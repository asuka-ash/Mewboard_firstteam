#include <stdio.h> // standard input output
#include <sys/types.h> // system call types
#include <sys/socket.h> // socket data types
#include <netinet/in.h> // internet domain types
#include <iostream>
#include <unistd.h>
#include <netdb.h>
#include <string>
#include <string.h>

// Create A Port
// Bind the Socket to IP / PORT
// Markt the socket to listen
// Accept a call
// Close the listening Socket
// While recieving display message, echo message
// Close socket

using namespace std;

int main(int argc, const char** argv) {

    int listening = socket(AF_INET, SOCK_STREAM, 0);
    if (listening == -1) {
        cerr << "Can't create a socket!";
        return -1;
    }else{
        cout << "Socket Created:" << listening << endl;
    }

    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(5000);
    
    return 0;
}
