FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/customman/man1
RUN echo '.TH CUSTOMTOOL 1 "2024-06-01" "customtool manual"' > /home/user/customman/man1/customtool.1
RUN mkdir -p /home/user/bin
RUN echo '#!/bin/bash
echo custom' > /home/user/bin/customtool
RUN chmod +x /home/user/bin/customtool
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

