FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project
RUN mkdir -p /home/user/reports
RUN printf "Draft version 2.1\nReviewed by Alice\n" > /home/user/reports/draft_report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

