FROM unix101-base:latest

USER root
RUN printf "Network up\nNetwork down\nnetwork issue detected\nAll systems operational\nNETWORK restored\nPartial network outage\nNo problems found\n" > /home/user/network_status.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

