FROM unix101-base:latest

USER root
RUN printf "Executive Summary\nAll targets achieved." > /home/user/summary.txt
RUN mkdir -p /home/user/docs
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

