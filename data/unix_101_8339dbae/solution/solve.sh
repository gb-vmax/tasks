#!/bin/bash
csplit -s -f session_ -n 3 /home/user/server.log '/=== SESSION START ===/' '{*}'
