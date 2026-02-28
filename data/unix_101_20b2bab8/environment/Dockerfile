FROM unix101-base:latest

USER root
RUN echo -e 'The cat sat on the mat.\nA black cat ran away.' > /home/user/story.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

