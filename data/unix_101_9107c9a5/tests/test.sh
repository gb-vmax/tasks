#!/bin/bash
pass=1
for f in \
  /home/user/pictures/old_image1.jpg \
  /home/user/pictures/vacation/old_beach.jpg \
  /home/user/pictures/vacation/old_sunset.jpg \
  /home/user/pictures/events/old_birthday.jpg; do
  if [ ! -f "$f" ]; then
    pass=0
  fi
done
for f in \
  /home/user/pictures/image1.jpg \
  /home/user/pictures/vacation/beach.jpg \
  /home/user/pictures/vacation/sunset.jpg \
  /home/user/pictures/events/birthday.jpg; do
  if [ -f "$f" ]; then
    pass=0
  fi
done
if [ -f /home/user/pictures/sample.png ] && [ -f /home/user/pictures/events/party.png ]; then
  echo $pass > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
