FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/test_false_easy
RUN echo 'This is a test for the false command.' > /home/user/test_false_easy/info.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

