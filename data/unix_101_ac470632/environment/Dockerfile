FROM unix101-base:latest

USER root
RUN echo '/home/user/documents/reports/annual.txt' > /home/user/paths.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

