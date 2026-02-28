FROM unix101-base:latest

USER root
RUN echo -e 'Alpha\nBravo\nCharlie\nDelta\nEcho\nFoxtrot\nGolf' > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

