FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf 'The quick brown fox jumps over the lazy dog\nPack my box with five dozen liquor jugs.\n' > /home/user/data/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

