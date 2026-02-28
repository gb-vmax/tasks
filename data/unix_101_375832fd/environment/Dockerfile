FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf "ID\tName\tScore\n1\tAlice\t98\n2\tBob\t87\n" > /home/user/data/scores.tsv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

