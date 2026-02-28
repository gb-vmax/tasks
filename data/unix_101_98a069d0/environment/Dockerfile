FROM unix101-base:latest

USER root
RUN echo 's(1)' > /home/user/sin_input.txt
RUN rm -f /home/user/sin_result.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

