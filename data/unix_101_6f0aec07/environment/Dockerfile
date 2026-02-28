FROM unix101-base:latest

USER root
RUN cd /home/user
RUN echo 'Hello World' > file1.txt
RUN echo 'Second file' > file2.txt
RUN zip archive.zip file1.txt file2.txt
RUN rm file1.txt file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

