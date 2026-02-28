FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN mkdir -p /home/user/docs
RUN echo 'Build finished successfully.' > /home/user/logs/build.log
RUN rm -f /home/user/docs/latest.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

