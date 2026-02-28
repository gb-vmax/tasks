FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN printf '2024-06-01 10:00:01 Start\n2024-06-01 10:01:02 Processing\n2024-06-01 10:02:03 Finished\n' > /home/user/logs/app.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

