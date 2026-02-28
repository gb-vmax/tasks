FROM unix101-base:latest

USER root
RUN printf "apple\nbanana\ncarrot\ndate\n" > /home/user/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

