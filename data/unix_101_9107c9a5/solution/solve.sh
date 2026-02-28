#!/bin/bash
rename -v 's|(.*)/(.*\.jpg)$|$1/old_$2|' /home/user/pictures/**/*.jpg /home/user/pictures/*.jpg
