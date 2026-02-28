FROM unix101-base:latest

USER root
RUN echo -e 'Alice\nBob\nCarol\nDave' > /home/user/names.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

