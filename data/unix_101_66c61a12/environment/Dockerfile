FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN bash -c 'sleep 1000 & echo $! > /home/user/echo.pid'
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

