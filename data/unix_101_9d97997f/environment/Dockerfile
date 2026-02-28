FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e 'First Line\nSecond\nThird line' > /home/user/alpha.txt
RUN echo -e 'first   line\nSECOND\nthird  line ' > /home/user/beta.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

