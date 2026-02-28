FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/photos/camera1
RUN mkdir -p /home/user/photos/camera2
RUN printf 'image data\n' > /home/user/photos/camera1/img001.jpg
RUN printf 'image data\n' > /home/user/photos/camera2/img001.jpg
RUN printf 'other data\n' > /home/user/photos/camera1/img002.jpg
RUN printf 'different\n' > /home/user/photos/camera2/img002.jpg
RUN printf 'image data\n' > /home/user/photos/camera2/img003.jpg
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

