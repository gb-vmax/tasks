FROM unix101-base:latest

USER root
RUN printf "alpha\nbeta\ngamma\ndelta\nepsilon\n" > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

