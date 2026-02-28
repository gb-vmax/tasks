FROM unix101-base:latest

USER root
RUN printf "pear\napple\nbanana\norange\n" > /home/user/unsorted.txt
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

