FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/dirA /home/user/dirB
RUN printf "Hello World\n" > /home/user/dirA/file1.txt
RUN printf "Hello World!\n" > /home/user/dirB/file1.txt
RUN printf "Another file\n" > /home/user/dirA/file2.txt
RUN printf "Another file\n" > /home/user/dirB/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

