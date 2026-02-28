FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cp /var/run/utmp /home/user/test_utmp
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

