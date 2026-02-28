FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -e 'Alice\nBob\nCharlie' > /home/user/data/names.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

