#!/bin/bash
parallel echo {} ::: apple banana cherry > /home/user/parallel_output.txt
