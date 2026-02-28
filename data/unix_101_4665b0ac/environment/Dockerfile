FROM unix101-base:latest

USER root
RUN echo '111 First line' > /home/user/part1.txt
RUN echo '222 Second line' >> /home/user/part1.txt
RUN xz /home/user/part1.txt
RUN echo '333 Third line' > /home/user/part2.txt
RUN echo '444 Fourth line' >> /home/user/part2.txt
RUN xz /home/user/part2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

