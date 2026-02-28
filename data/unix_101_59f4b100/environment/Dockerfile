FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN touch /home/user/startmarker
RUN su user -c 'nohup sleep 300 > /home/user/sleep1.out 2>&1 &'
RUN su user -c 'nohup sleep 200 > /home/user/sleep2.out 2>&1 &'
RUN su user -c 'nohup sleep 100 > /home/user/sleep3.out 2>&1 &'
RUN sleep 1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

