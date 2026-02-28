FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN echo 'First log entry' > /home/user/logs/part1.log
RUN echo 'Second log entry' > /home/user/logs/part2.log
RUN xz -z -k /home/user/logs/part1.log
RUN xz -z -k /home/user/logs/part2.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

