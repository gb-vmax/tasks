FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/photos/2022
RUN mkdir -p /home/user/music/album
RUN touch /home/user/photos/2022/vacation.jpg
RUN touch /home/user/music/album/song.mp3
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

