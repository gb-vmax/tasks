FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

# Create /home/user/build_output and its v4 subdirectory
install -d -m 755 /home/user/build_output/v4

# Top-level files in /home/user/build_output
touch /home/user/build_output/libmath.a
touch /home/user/build_output/main.o
touch /home/user/build_output/utils.o
touch /home/user/build_output/build.log
touch /home/user/build_output/results.tmp
touch /home/user/build_output/readme.txt

# Files in /home/user/build_output/v4
touch /home/user/build_output/v4/math.o
touch /home/user/build_output/v4/parse.o
touch /home/user/build_output/v4/datagen.tmp
touch /home/user/build_output/v4/test.tar.gz

# DO NOT create obj_archive or move-log.txt yet

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
