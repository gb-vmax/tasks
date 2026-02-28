FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -n 'foo bar' > /home/user/data.txt
RUN rm -f /home/user/result.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

