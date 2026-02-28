FROM unix101-base:latest

USER root
RUN echo 'export MY_ENV_VAR=hello_world' >> /home/user/.bashrc
RUN echo 'export MY_ENV_VAR=hello_world' > /home/user/envtest.sh
RUN echo 'echo $MY_ENV_VAR' >> /home/user/envtest.sh
RUN chmod +x /home/user/envtest.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

