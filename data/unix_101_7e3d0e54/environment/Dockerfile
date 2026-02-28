FROM unix101-base:latest

USER root
RUN rm -rf /home/user/*
RUN mkdir -p /home/user
RUN echo -e '15\n100\n77' > /home/user/numbers.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

