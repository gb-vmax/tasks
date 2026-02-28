FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'alpha' > /home/user/a.txt
RUN echo -e 'beta\ngamma' > /home/user/b.txt
RUN echo -e 'delta\nepsilon\nzeta' > /home/user/c.txt
RUN echo '/home/user/a.txt,/home/user/b.txt,/home/user/c.txt' > /home/user/files.csv
RUN rm -f /home/user/linecounts.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

