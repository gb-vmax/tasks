FROM unix101-base:latest

USER root
RUN echo Alpha > /home/user/data.txt
RUN echo Beta >> /home/user/data.txt
RUN echo Gamma >> /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

