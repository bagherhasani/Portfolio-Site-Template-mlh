#!/bin/bash

URL="http://127.0.0.1:5001/api/timeline_post" # I used port 5001 cause port 5000 is for built in mac services.
RANDOM_ID=$RANDOM
CONTENT="test post $RANDOM_ID"

echo "potsing random data . .."

curl -s -X POST "$URL" \
-d "name=Baker" \
-d "email=test$RANDOM_ID@example.com" \
-d "content=$CONTENT"

echo
echo "checking get endpoint..."

RESULT=$(curl -s "$URL")

if echo "$RESULT" | grep -q "$CONTENT"; then
    echo "sucess, post was added"
else
    echo "failed, post not found"
    exit 1
fi