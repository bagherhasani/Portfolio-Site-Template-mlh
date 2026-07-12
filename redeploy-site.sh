#!/bin/bash

#kill the tmux sessions
tmux kill-server 2>/dev/null

#navigate to the portfolio site directory
cd ~/Portfolio-Site-Template-mlh

#get with git -- I will change it to main after merging but for now it's origin/feature/enhance-ui branch
git fetch
git reset origin/feature/enhance-ui  --hard


# activate vm
source python3-virtualenv/bin/activate

#install requiremtns
pip install -r requirements.txt

#start a flask seesion
tmux new-session -d -s flask-server "cd ~/Portfolio-Site-Template-mlh && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"

