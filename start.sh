#!/bin/sh
cat << "EOF"
                            ____ _               _   
                           / ___| |__   ___  ___| |_ 
                          | |  _| '_ \ / _ \/ __| __|
                          | |_| | | | | (_) \__ \ |_ 
                           \____|_| |_|\___/|___/\__|
                            A Code by sanat gupta
EOF
  echo "starting onion router..."
  echo "establishing connection.."
  sudo python3 torghost.py -s
  echo "onion router configured and started!"
  echo "starting browser..."
  echo "running happy privacy!"
  python3 pythonbrowser.py
 





