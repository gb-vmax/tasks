FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "HELLO=world\n" > /home/user/custom_env.txt
RUN export ABC=123
RUN export DEF=456
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

