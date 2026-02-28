FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'TESTVAR=foo' >> /home/user/.bashrc
RUN echo 'export TESTVAR' >> /home/user/.bashrc
RUN echo 'export ANOTHERVAR=bar' >> /home/user/.bashrc
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

