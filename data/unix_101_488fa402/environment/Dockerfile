FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/input
RUN mkdir -p /home/user/output
RUN echo 'SGVsbG8sIHdvcmxkIQ== # some comment' > /home/user/input/encoded_with_garbage.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

