FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project
RUN touch /home/user/project/README
RUN touch /home/user/project/verylongfilenameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
RUN touch /home/user/project/illegal:name
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

