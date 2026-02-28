FROM unix101-base:latest

USER root
RUN echo 'Project Data 2024' > /home/user/data.txt
RUN rm -f /home/user/archive.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

