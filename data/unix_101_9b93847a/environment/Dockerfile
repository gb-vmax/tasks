FROM unix101-base:latest

USER root
RUN touch /home/user/lockfile.lock
RUN printf "existing1\nexisting2\n" > /home/user/lockfile.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

