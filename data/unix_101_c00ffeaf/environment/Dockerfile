FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -e "file1\t1024\tinfoA\nfile2\t2048\tinfoB\nfile3\t1048576\tinfoC" > /home/user/data/report.tsv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

