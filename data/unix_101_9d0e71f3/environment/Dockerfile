FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf 'apple\nbanana\ncarrot\n' > /home/user/data/food.txt
RUN printf 'dog\nelephant\nfrog\n' > /home/user/data/animals.txt
RUN printf 'red\nblue\ngreen\n' > /home/user/data/colors.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

