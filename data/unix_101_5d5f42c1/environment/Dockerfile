FROM unix101-base:latest

USER root
RUN echo 'Sample text file' > /home/user/file1.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

