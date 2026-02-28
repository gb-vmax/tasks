FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n1234567890abcdefghij\n" > /home/user/data/alpha.txt
RUN printf "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\n" > /home/user/data/beta.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

