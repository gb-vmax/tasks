FROM unix101-base:latest

USER root
RUN echo -e 'Once upon a time,\nthere was a penguin.\nIt loved Linux.' > /home/user/story.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

