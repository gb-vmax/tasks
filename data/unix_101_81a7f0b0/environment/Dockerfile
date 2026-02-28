FROM unix101-base:latest

USER root
RUN echo -e 'beacon\nBeagle\nbeat\nBEAR\nBee\nbelieve\nBelow\nBend\nbench\nBean\nboat\nBerry' > /home/user/Wordlist.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

