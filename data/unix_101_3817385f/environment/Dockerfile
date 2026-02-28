FROM unix101-base:latest

USER root
RUN echo 'The quick brown fox jumps over the lazy dog.' > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

