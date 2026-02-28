FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e 'A\nB\nC\nD' > /home/user/old.txt
RUN echo -e 'A\nB\nCX\nD' > /home/user/new.txt
RUN echo -e 'A\nBY\nC\nD' > /home/user/my.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

