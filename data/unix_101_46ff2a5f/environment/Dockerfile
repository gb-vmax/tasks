FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN echo 'hello world' > /home/user/file.txt
RUN echo 'reference data' > /home/user/reference.txt
RUN touch -t 202201010101.01 /home/user/reference.txt
RUN touch -t 202212312359.59 /home/user/file.txt
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

