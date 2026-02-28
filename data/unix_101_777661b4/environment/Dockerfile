FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/bin
RUN mkdir -p /home/user/src
RUN mkdir -p /home/user/man/man1
RUN echo '#!/bin/bash
echo Hello' > /home/user/bin/mycmd
RUN chmod +x /home/user/bin/mycmd
RUN echo 'int main() { return 0; }' > /home/user/src/mycmd.c
RUN echo '.TH MYCMD 1 "2024-06-01" "mycmd manual"' > /home/user/man/man1/mycmd.1
RUN export PATH=/home/user/bin:$PATH
RUN export MANPATH=/home/user/man:$MANPATH
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

