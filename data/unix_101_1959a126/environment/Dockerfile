FROM unix101-base:latest

USER root
RUN touch /home/user/my_valid_file.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

