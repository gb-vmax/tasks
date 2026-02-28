FROM unix101-base:latest

USER root
RUN groupadd -f devs
RUN useradd -M -g devs developer || true
RUN mkdir -p /home/user/project/docs
RUN echo 'main source' > /home/user/project/main.c
RUN echo 'documentation' > /home/user/project/docs/readme.md
RUN touch /home/user/project/.env
RUN chown -R user:user /home/user/project
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

