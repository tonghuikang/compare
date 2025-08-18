nohup python3 -m http.server 64088 > server.log 2>&1 &
sleep 3
cat server.log
