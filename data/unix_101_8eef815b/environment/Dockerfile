FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "apple\nbanana\napple pie\norange\napple juice\n" > /home/user/fruits.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

