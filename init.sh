#!/bin/bash

# Remove old logs
python service/start_msg.py
if [ -f 'logs.txt' ]; then
  rm 'Logs.txt'
fi


python service/chatbot_service.py 2> logs/logs.txt &
python service/summary_service.py 2> logs/logs.txt &

# Wait for any process to exit
wait -n

exit $?