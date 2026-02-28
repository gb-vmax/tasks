FROM unix101-base:latest

USER root
RUN echo -e 'alpha\nbeta\ngamma\ndelta\nepsilon\nzeta' > /home/user/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

