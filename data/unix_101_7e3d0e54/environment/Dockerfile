FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "45\n60\n97\n100\n" > /home/user/nums.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

