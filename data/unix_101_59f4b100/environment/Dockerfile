FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN su - user -c 'nohup sleep 1000 > /home/user/sleep1.out 2>&1 &'
RUN su - user -c 'nohup sleep 1001 > /home/user/sleep2.out 2>&1 &'
RUN su - user -c 'nohup tail -f /dev/null > /home/user/tail1.out 2>&1 &'
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

