FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN printf 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8\nLine 9\nLine 10\n' > /home/user/logs/app.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

