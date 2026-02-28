FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/projects/test
RUN echo "Important project file" > /home/user/file.txt
RUN ln -s ../file.txt /home/user/projects/test/link1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

