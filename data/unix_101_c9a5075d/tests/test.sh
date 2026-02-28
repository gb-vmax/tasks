#!/bin/bash
expected=$'/home/user/photos/2022\0/home/user/music/album'
output=$(dirname -z /home/user/photos/2022/vacation.jpg /home/user/music/album/song.mp3)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
