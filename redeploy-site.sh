#!/bin/bash

#kill the tmux sessions
#tmux kill-server 2>/dev/null

#navigate to the portfolio site directory
cd ~/Portfolio-Site-Template-mlh

#get with git -- I will change it to main after merging but for now it's origin/feature/enhance-ui branch
git fetch origin
git reset origin/main --hard


# activate vm
source python3-virtualenv/bin/activate

#install requiremtns
pip install -r requirements.txt

#systemd restart the service
systemctl restart myportfolio.service

# lets show if the restart was successful
systemctl status myportfolio.service --no-pager