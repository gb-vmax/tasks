FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo 'Hello World' > /home/user/data/greeting.txt
RUN echo '42' > /home/user/data/answer.txt
RUN cd /home/user && zip -r example.zip data/
RUN rm -rf /home/user/data
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

