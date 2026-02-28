FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo 'Sample data' > /home/user/data/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

