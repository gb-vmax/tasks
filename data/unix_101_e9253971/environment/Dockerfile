FROM unix101-base:latest

USER root
RUN echo -e 'A B\nB C\nC D' > /home/user/deps.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

