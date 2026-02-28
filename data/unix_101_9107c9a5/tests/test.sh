#!/bin/bash
if [ -f /home/user/images/old_img1.jpg ] && [ -f /home/user/images/old_img2.jpg ] && [ ! -f /home/user/images/img1.jpg ] && [ ! -f /home/user/images/img2.jpg ] && grep -q 'data1' /home/user/images/old_img1.jpg && grep -q 'data2' /home/user/images/old_img2.jpg && [ -f /home/user/images/photo.jpg ] && [ ! -f /home/user/images/old_photo.jpg ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
