FROM unix101-base:latest

USER root
RUN printf "apple\nbanana\ncherry\ndate\nfig\n" > /home/user/alpha.txt
RUN printf "banana\ncherry\nfig\ngrape\n" > /home/user/beta.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

