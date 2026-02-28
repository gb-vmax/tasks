FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/pictures/vacation
RUN mkdir -p /home/user/pictures/events
RUN touch /home/user/pictures/image1.jpg
RUN touch /home/user/pictures/vacation/beach.jpg
RUN touch /home/user/pictures/vacation/sunset.jpg
RUN touch /home/user/pictures/events/birthday.jpg
RUN touch /home/user/pictures/events/party.png
RUN touch /home/user/pictures/sample.png
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

