FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo "custom-agent-host" > /home/user/newhostname.txt
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

