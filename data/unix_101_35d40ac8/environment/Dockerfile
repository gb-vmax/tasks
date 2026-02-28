FROM unix101-base:latest

USER root
RUN echo 'This is the target file.' > /home/user/target1.txt
RUN ln -s /home/user/target1.txt /home/user/link1
RUN rm -f /home/user/result.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

