FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN rm -f /home/user/lc_time_keywords.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

