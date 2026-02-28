FROM unix101-base:latest

USER root
RUN groupadd testgrp1
RUN groupadd testgrp2
RUN usermod -a -G testgrp1,user,testgrp2 user
RUN mkdir -p /home/user
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

