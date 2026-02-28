FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'alias gs="git status"' >> /home/user/.bashrc
RUN echo 'alias ll="ls -l"' >> /home/user/.bashrc
RUN echo 'alias la="ls -a"' >> /home/user/.bashrc
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

