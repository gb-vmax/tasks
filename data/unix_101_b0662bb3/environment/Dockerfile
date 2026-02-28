FROM unix101-base:latest

USER root
RUN printf 'Roses are red\nViolets are blue\nSugar is sweet\nAnd so are you\nThis is a poem\nFor you to read\nHope you enjoy\nIndeed indeed\n' > /home/user/poem.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

