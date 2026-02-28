FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/photos
RUN echo 'holiday photo 1' > /home/user/photos/img1.jpg
RUN echo 'holiday photo 1' > /home/user/photos/img2.jpg
RUN echo 'holiday photo 2' > /home/user/photos/img3.jpg
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

