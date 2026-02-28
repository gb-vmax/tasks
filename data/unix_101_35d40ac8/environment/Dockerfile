FROM unix101-base:latest

USER root
RUN echo 'Hello, world!' > /home/user/file1.txt
RUN ln -s /home/user/file1.txt /home/user/link1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

