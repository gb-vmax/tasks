FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project
RUN printf 'Template file\n' > /home/user/project/template.txt
RUN sleep 2
RUN printf 'Some notes\n' > /home/user/project/notes.txt
RUN touch -d '2022-12-31 15:00:00' /home/user/project/template.txt
RUN touch -d '2020-01-01 10:00:00' /home/user/project/notes.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

