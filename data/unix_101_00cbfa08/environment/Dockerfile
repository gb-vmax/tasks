FROM unix101-base:latest

USER root
RUN printf "abcdef\nghijkl\nmnopqr\nstuvwx\n" > /home/user/phrases.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

