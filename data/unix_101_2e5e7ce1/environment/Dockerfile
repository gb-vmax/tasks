FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'export MYVAR=secretvalue' >> /etc/profile.d/testenv.sh
RUN chmod +x /etc/profile.d/testenv.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

