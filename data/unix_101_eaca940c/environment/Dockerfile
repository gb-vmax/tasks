FROM unix101-base:latest

USER root
RUN touch /home/user/lockfile.lock
RUN printf "initial\n" > /home/user/output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

