FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN touch /home/user/.bash_history
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

