FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'Alice saw the white rabbit hurry down the hole.' > /home/user/old.txt
RUN echo 'Alice quickly saw the white rabbit hurry down the hole.' > /home/user/new.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

