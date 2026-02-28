FROM unix101-base:latest

USER root
RUN printf 'name,age,city\nAlice,30,Paris\nBob,25,Berlin\nCharlie,40,Rome\nDiana,22,Madrid\n' > /home/user/data.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

