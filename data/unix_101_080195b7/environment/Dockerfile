FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "alpha\nline two\n" > /home/user/alpha.txt
RUN printf "beta\nsecond line\nthird line\n" > /home/user/beta.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

