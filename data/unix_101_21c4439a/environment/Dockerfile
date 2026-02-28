FROM unix101-base:latest

USER root
RUN echo -e 'John,24\nAlice,30\nEve,22\nBob,27' > /home/user/data.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

