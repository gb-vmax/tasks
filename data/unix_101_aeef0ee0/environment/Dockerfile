FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/alpha
RUN mkdir -p /home/user/project/beta/gamma
RUN touch /home/user/project/file1.txt
RUN echo 'Data' > /home/user/project/file2.txt
RUN touch /home/user/project/alpha/empty1.log
RUN echo 'Not empty' > /home/user/project/alpha/data2.csv
RUN touch /home/user/project/beta/empty2.md
RUN echo 'Content' > /home/user/project/beta/gamma/data3.txt
RUN touch /home/user/project/beta/gamma/empty3.tmp
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

