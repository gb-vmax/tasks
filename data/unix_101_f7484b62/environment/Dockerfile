FROM unix101-base:latest

USER root
RUN echo -n 'short' > /home/user/input.txt
RUN echo -n '1234567890' > /home/user/ref.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

