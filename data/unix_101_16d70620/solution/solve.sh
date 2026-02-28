#!/bin/bash
parallel sed -i 's/foo/bar/g' ::: /home/user/texts/file1.txt /home/user/texts/file2.txt /home/user/texts/file3.txt
