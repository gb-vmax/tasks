FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/real_folder
RUN ln -s /home/user/real_folder /home/user/link_folder
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

