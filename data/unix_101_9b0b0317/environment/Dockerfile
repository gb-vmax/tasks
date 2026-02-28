FROM unix101-base:latest

USER root
RUN printf "An apple\nbanana split\nUnder the sun\nElephant parade\norange juice\nIguana island\numbrella\nDog day\nEgg salad\n" > /home/user/phrases.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

