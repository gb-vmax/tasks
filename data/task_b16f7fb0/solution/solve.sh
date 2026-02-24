#!/bin/bash
# Ground truth reference (not an executable solution):
#
# /home/user/provisioning/configs must exist and be a directory.
# /home/user/provisioning/configs/web.conf must contain only: WEB.CONF (with a single line, no extra whitespace)
# /home/user/provisioning/configs/db.conf must contain only: DB.CONF (with a single line, no extra whitespace)
# /home/user/provisioning/configs/cache.conf must contain only: CACHE.CONF (with a single line, no extra whitespace)
# /home/user/provisioning/active must exist and be a directory.
# 
# /home/user/provisioning/active/web_active.conf must exist and be a symlink, with target ../configs/web.conf
# /home/user/provisioning/active/db_active.conf must exist and be a symlink, with target ../configs/db.conf
# /home/user/provisioning/active/cache_active.conf must exist and be a symlink, with target ../configs/cache.conf
# 
# The symlinks must be relative (i.e., their link target path must begin with ../).
# 
# /home/user/provisioning/symlink_report.txt must exist and have exact contents (no extra whitespace or blank lines):
# 
# web_active.conf,../configs/web.conf,WEB.CONF
# db_active.conf,../configs/db.conf,DB.CONF
# cache_active.conf,../configs/cache.conf,CACHE.CONF

echo 'No automated solution provided.'
