FROM unix101-base:latest

USER root
RUN printf "Apple pie\nbanana bread\nAPPLE juice\nOrange\napple tart\nPeach\n" > /home/user/fruits.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

