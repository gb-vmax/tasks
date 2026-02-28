#!/bin/bash
join -t, -1 2 -2 1 -o 1.1,2.2 /home/user/people.csv /home/user/cities.csv > /home/user/matches.csv
