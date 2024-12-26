#!/bin/bash

tmux new-session -d -s dev_env -n mock

tmux split-window -h -t dev_env:0

tmux send-keys -t dev_env:0.0 'cd extension && npm run dev' C-m

tmux send-keys -t dev_env:0.1 'cd backend && npm run dev' C-m

tmux send-keys -t dev_env:0.1 'echo "This is Pane 1"' C-m
