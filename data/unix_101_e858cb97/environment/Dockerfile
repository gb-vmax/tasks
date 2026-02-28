FROM unix101-base:latest

USER root
RUN echo 'greet() { echo Hello; }' >> /home/user/.bashrc
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

