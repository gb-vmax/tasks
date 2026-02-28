FROM unix101-base:latest

USER root
RUN echo -e '2024-06-01 10:00:00 System booted\n2024-06-01 10:01:00 Service started' > /home/user/system.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

