#!/bin/bash
cp /home/user/data/info.log /home/user/data/info.log.bak && tr 'a-z' 'A-Z' < /home/user/data/info.log | sponge /home/user/data/info.log
