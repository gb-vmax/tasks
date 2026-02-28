FROM unix101-base:latest

USER root
RUN echo -e 'Hello\nWorld\nABCDE' > /home/user/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

