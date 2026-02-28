FROM unix101-base:latest

USER root
RUN printf "A B\nB C\nD C\nE D\n" > /home/user/order.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

