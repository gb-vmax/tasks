FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/ls_longtest/subdir
RUN touch /home/user/ls_longtest/fileA.txt
RUN touch /home/user/ls_longtest/fileB.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

