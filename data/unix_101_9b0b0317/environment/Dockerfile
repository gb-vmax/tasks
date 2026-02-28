FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/texts
RUN echo 'She started singing and danced around.' > /home/user/texts/first.txt
RUN echo 'He jumped while running and played chess.' > /home/user/texts/second.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

