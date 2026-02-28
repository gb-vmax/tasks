FROM unix101-base:latest

USER root
RUN echo -e 'hello world\nthis is a test\nend of file' > /home/user/fileA.txt
RUN cp /home/user/fileA.txt /home/user/fileB.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

