FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf 'Start log\nInitial entry\n' > /home/user/log.txt
RUN printf 'Second entry\nFinal entry\n' > /home/user/update.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

