FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Confidential report content' > /home/user/docs/report.txt
RUN chown -R user:user /home/user
RUN su - user -c "bash -c 'tail -f /home/user/docs/report.txt > /dev/null &'"
RUN sleep 1
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

