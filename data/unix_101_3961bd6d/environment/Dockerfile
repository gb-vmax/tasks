FROM unix101-base:latest

USER root
RUN printf "This is a project file.\n" > /home/user/project.txt
RUN chown root:root /home/user/project.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

