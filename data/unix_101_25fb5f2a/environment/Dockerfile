FROM unix101-base:latest

USER root
RUN printf 'export MYVAR=hello\n' > /home/user/env_setup.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

