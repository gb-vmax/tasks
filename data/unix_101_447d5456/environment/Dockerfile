FROM unix101-base:latest

USER root
RUN echo 'Real data file.' > /home/user/data.txt
RUN ln -s /home/user/data.txt /home/user/link_to_data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

