FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/dirA /home/user/dirB
RUN echo 'target file' > /home/user/dirB/realfile.txt
RUN ln -s ../dirB/realfile.txt /home/user/dirA/link2
RUN ln -s link2 /home/user/dirA/chainlink
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

