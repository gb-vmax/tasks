FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo 'Hello, bzip2 world!' > /home/user/data/hello.txt
RUN bzip2 -k /home/user/data/hello.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

