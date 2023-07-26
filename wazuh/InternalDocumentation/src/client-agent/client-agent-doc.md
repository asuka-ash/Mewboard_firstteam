# File Structure
```
|-- agcom.c
|-- agentd.c
|-- agentd.h
|-- buffer.c
|-- config.c
|-- event-forward.c
|-- main.c 
|-- notify.c
|-- receiver.c
|-- request.c
|-- restart_agent.c
|-- rotate_log.c
|-- sendmsg.c
|-- start_agent.c
|-- state.c
`-- state.h
```
# File: main.c 
'''
Entry Point to Agent Creation
'''

> includes: [shared.h, agentd.h]

1. help_agentd(): prints info, frees installation path

2. main(): argv[0]: homepath
   1. change path to install directory
   2. define agent from client-config.h
   3. checks debug flags
   4. Checks Config file for OS compatibility: config.c
   5. checks if the server rip, port, interface, protocol etc. are set for agent
   6. checks if the address is valid, string should not ve MANAGER or 0.0.0.0
   7. sets up signals for the agent process
   8. Starts the agent process, for uid, gid, user = wazuh, and group = wazuh by calling AgentdStart

# Files: agentd.c, rotate_log.c, buffer.c, request.c

1. AgentdStart(uid, gid, user, group)
   1. Starts the agent daemon
   2. checks if should run in foreground or not
   3. sets group and user ids.
   4. checks if auth keys are present
   5. attempts to connect with the server
   6. Periodically sends notifications to the server
   7. Sets an agent stop message atExit.
   8. Starts Several Threads
      1.  Rotation Thread:
          1.  This code is a log rotation thread that periodically checks log files for rotation based on specified criteria like file size and daily rotation. It compresses and rotates log files if they reach a certain size or if a new day begins. It runs as a thread and performs the log rotation process while the main program continues its execution.
          2.  File: src/client-agent/rotate_log.c 
   
      2.  Dispatch Thread:
          1.  This code implements an anti-flooding mechanism for log messages in a program. It manages a buffer that stores log messages and monitors the buffer usage. When the buffer reaches certain levels (normal, warning, full, or flooded), it takes appropriate actions such as sending warning messages, compressing logs, or discarding events to prevent flooding. The code utilizes multi-threading to handle the buffer and message dispatching efficiently.
          2.  File: src/client-agent/buffer.c
   
      3.  Statistics Thread: 
          1.  This code defines and implements functions for managing the state of an agent, including updating and writing the agent's state to a state file. It uses multi-threading to periodically update the state file with relevant information such as agent status, last keep-alive time, last ACK time, number of generated events, messages sent, and the number of events currently buffered. The state is represented as a C struct, and the code provides functions to initialize, update, and retrieve the agent's state information in a JSON format.
          2.  File: src/client-agent/state.c

      4.  Request Received Thread:
          1.  This code implements a request manager that handles incoming requests and forwards them to the appropriate target socket for processing. It uses a hash table to keep track of active requests and a request pool to manage concurrent request handling. The code also handles sending responses back to the manager, including waiting for ACKs in UDP mode. The target socket is determined based on the request type (e.g., "agent", "logcollector", etc.). The code uses multi-threading to handle incoming requests concurrently.
          2.  File: src/agent-client/request.c



