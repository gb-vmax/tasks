FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf '6 * 7 + 4\n' > /home/user/calc.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

