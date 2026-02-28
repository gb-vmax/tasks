FROM unix101-base:latest

USER root
RUN printf "apple\nbanana\ncherry\n" > /home/user/patterns.txt
RUN printf "I like apple pie\nBanana bread is tasty\nCherries are red\nGrape juice is nice\napple and banana together\n" > /home/user/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

