FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e "10\n20\n30\n40\n50" > /home/user/numbers1.txt
RUN echo -e "20\n30\n60\n70" > /home/user/numbers2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

