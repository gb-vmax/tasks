FROM unix101-base:latest

USER root
RUN echo 'Started application' > /home/user/app.log
RUN echo 'User 123 logged in' >> /home/user/app.log
RUN echo 'Error: code 404' >> /home/user/app.log
RUN echo 'Shutdown complete' >> /home/user/app.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

