FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/texts
RUN echo 'foo' > /home/user/texts/file1.txt
RUN echo 'foo' > /home/user/texts/file2.txt
RUN echo 'foo' > /home/user/texts/file3.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

