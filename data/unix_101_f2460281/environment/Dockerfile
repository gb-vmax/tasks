FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo '# Custom dircolors file' > /home/user/mycolors.txt
RUN echo 'DIR 35' >> /home/user/mycolors.txt
RUN echo 'LINK 36' >> /home/user/mycolors.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

