FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' > /home/user/data/paragraph.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

