FROM unix101-base:latest

USER root
RUN echo -e 'banana\napple pie\ncherry\napple\npear\napple tart' > /home/user/fruits.txt
RUN rm -f /home/user/found_apples.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

