#!/bin/bash
rsync -r --exclude='*.log' /home/user/project_src/ /home/user/project_backup/
