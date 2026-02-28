#!/bin/bash
inode1=$(stat -c '%i' /home/user/photos/camera1/img001.jpg)
inode2=$(stat -c '%i' /home/user/photos/camera2/img001.jpg)
inode3=$(stat -c '%i' /home/user/photos/camera1/img002.jpg)
inode4=$(stat -c '%i' /home/user/photos/camera2/img002.jpg)
inode5=$(stat -c '%i' /home/user/photos/camera2/img003.jpg)
if [ "$inode1" = "$inode2" ] && [ "$inode3" != "$inode4" ] && [ "$inode1" != "$inode5" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
