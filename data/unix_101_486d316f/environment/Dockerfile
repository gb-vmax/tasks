FROM unix101-base:latest

USER root
RUN echo -n 'abcdefghij1234567890ABCDEFGHIJ' > /home/user/data.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

