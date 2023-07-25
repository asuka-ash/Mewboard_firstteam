## Steps to test the docker setup

1. Build the Docker image using the command 
   <docker build -t wazuh .>

2. Start a container from the image using the command "docker run -it --rm --name wazuh_test -v /Users/dheeraj/MewBoard/Mewboard/wazuh:/home/developer/tool wazuh".
   
3. We will follow similar setup for all the features that we develop

# Step:1 Exploring Source Code
## Using CSCOPE to explore the source code
```
find . -name "*.c" -o -name "*.cpp" -o -name "*.py" -o -name "*.h" -o -name "*.sh" -o -name "*.hpp" > cscope.files
```

## pass the list of source files to Cscope, which will build a reference database
```
cscope -q -R -b -i cscope.files
```


