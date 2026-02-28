FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/src
RUN echo 'main(){}' > /home/user/project/src/main.c
RUN echo 'data' > /home/user/project/data.txt
RUN chmod 777 /home/user/project
RUN chmod 777 /home/user/project/src
RUN chmod 777 /home/user/project/src/main.c
RUN chmod 777 /home/user/project/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

