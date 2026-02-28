FROM unix101-base:latest

USER root
RUN echo -e 'first line\nsecond line\nthird line' > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

