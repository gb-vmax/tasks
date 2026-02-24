#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Before the task, the following files exist:
# 
# /home/user/localization/source.txt:
# Welcome
# Hello
# Save
# Exit
# 
# /home/user/localization/old_fr.txt:
# Welcome=Bienvenue
# Hello=Bonjour
# Exit=Sortie
# 
# After the agent completes the task, the following files must exist:
# 
# /home/user/localization/new_fr.txt:
# Welcome=Bienvenue
# Hello=Bonjour
# Save=
# Exit=Sortie
# 
# /home/user/localization/update.log:
# COPIED: Welcome
# COPIED: Hello
# MISSING: Save
# COPIED: Exit
# 
# There should be exactly four lines in each output file, corresponding to the order of source.txt. No extra spaces or lines.

echo 'No automated solution provided.'
