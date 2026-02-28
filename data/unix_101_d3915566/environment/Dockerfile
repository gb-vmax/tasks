FROM unix101-base:latest

USER root
RUN echo 'Real file contents.' > /home/user/realfile.txt
RUN ln -s /home/user/linkB /home/user/linkA
RUN ln -s /home/user/realfile.txt /home/user/linkB
RUN rm -f /home/user/canon.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

