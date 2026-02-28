FROM unix101-base:latest

USER root
RUN echo 'User1234 has 56 apples and 7890 oranges.' > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

