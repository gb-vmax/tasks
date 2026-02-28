FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN sudo -u user bash -c 'nohup sleep 300 >/dev/null 2>&1 &'
RUN sudo -u user bash -c 'nohup sleep 200 >/dev/null 2>&1 &'
RUN sudo -u user bash -c 'nohup sleep 100 >/dev/null 2>&1 &'
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

