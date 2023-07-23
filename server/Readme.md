## Steps to test the docker setup

1. Build the Docker image using the command 
   <docker build -t server .>

2. Start a container from the image using the command "docker run -it --rm --name mewboard_dev_con -v /Users/dheeraj/MewBoard/Mewboard/server:/home/developer/tool server".
   
3.  This command will automatically run make and then provide you with an interactive shell.

4. We will follow similar setup for all the features that we develop

Remember, these steps assume that Docker is already installed and that the Dockerfile and your code are in the current directory. Also, replace server and server_con with your desired image and container names respectively.