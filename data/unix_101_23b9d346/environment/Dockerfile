FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN date +%s.%N > /home/user/start_time_precise.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

