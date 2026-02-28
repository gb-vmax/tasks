FROM unix101-base:latest

USER root
RUN echo '7 + 13' > /home/user/input.txt
RUN rm -f /home/user/output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

