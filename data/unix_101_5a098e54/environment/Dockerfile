FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/photos
RUN echo 'photo1' > /home/user/photos/vacation1.jpg
RUN echo 'photo2' > /home/user/photos/vacation2.jpg
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

