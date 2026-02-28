FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo '/home/user/file1.txt
/home/user/file2.txt
/home/user/file3.txt' > /home/user/todelete.txt
RUN echo 'keep me' > /home/user/file1.txt
RUN echo 'remove me' > /home/user/file2.txt
RUN echo 'bye' > /home/user/file3.txt
RUN echo 'should stay' > /home/user/file4.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

