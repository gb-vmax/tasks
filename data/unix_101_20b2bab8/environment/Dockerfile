FROM unix101-base:latest

USER root
RUN printf "The cat sat on the mat.\nA black cat chased a rat.\nCats are curious creatures.\n" > /home/user/story.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

