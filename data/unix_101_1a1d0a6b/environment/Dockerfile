FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf "Roses are red\nViolets are blue\nSugar is sweet\nAnd so are you\n" > /home/user/data/poem.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

