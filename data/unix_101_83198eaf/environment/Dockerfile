FROM unix101-base:latest

USER root
RUN printf "abc123def\n456gh789i0j\nno_digits_here\n" > /home/user/mixed.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

