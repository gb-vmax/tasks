FROM unix101-base:latest

USER root
RUN printf "Alice\nalina\nAlison\nALICIA\nAlexander\nali\nAlina\nALINA\nalicia\nALI\nAlistair\nAlly\nAllan\nAllison\nAlina\nAli\nAlicia\nALIANA\nAlison\nAlina\nAlix\nAline\nAlina\nAlina\nAlison\nAlistair\nAlan\nAlva\nAlvin\nAlfred\nAl\nAlec\nAlba\nAlex\nAlexa\nAlexis\nAlia\nAlima\nAlin\nAlita\nAliyah\nalicja\nAlicja\n" > /home/user/names.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

