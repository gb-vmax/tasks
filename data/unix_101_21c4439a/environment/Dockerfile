FROM unix101-base:latest

USER root
RUN echo 42 > /home/user/scores.txt
RUN echo 7 >> /home/user/scores.txt
RUN echo 100 >> /home/user/scores.txt
RUN echo 58 >> /home/user/scores.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

