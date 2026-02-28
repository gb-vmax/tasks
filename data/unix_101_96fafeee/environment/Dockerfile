FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf 'Name\tAge\tCity\nAlice\t23\tParis\nBob\t30\tLondon\n' > /home/user/data/tabs.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

