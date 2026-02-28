FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/images
RUN echo 'data1' > /home/user/images/img1.jpg
RUN echo 'data2' > /home/user/images/img2.jpg
RUN echo 'photo' > /home/user/images/photo.jpg
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

