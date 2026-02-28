FROM unix101-base:latest

USER root
RUN printf "Alice\nBob\nCharlie\n" > /home/user/names.txt
RUN printf "23\n29\n31\n" > /home/user/ages.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

