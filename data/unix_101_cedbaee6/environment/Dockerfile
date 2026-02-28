FROM unix101-base:latest

USER root
RUN printf 'object1' > /home/user/alpha.o
RUN printf 'object2' > /home/user/beta.o
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

