#!/bin/bash
# Kill any existing server on port 64088
lsof -ti:64088 | xargs kill -9 2>/dev/null || true

# Start the Python server
nohup python3 server.py > server.log 2>&1 &
sleep 3
echo "Server started on http://localhost:64088/"
tail -n 20 server.log