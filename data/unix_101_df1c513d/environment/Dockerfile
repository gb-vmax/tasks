FROM unix101-base:latest

USER root
RUN printf "name,age,city\nJohn,23,London\nAlice,30,Paris\nBob,19,Berlin\n" > /home/user/data.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

