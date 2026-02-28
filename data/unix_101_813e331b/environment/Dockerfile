FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN printf 'Log Entry 1\nLog Entry 2\nLog Entry 3\n' > /home/user/logs/system.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

