FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data/reports
RUN printf "Report 1\n" > /home/user/data/reports/report1.txt
RUN printf "Report 2\n" > /home/user/data/reports/report2.txt
RUN printf "Main data file\n" > /home/user/data/datafile.txt
RUN chown root:root /home/user/data
RUN chown root:root /home/user/data/datafile.txt
RUN chown root:root /home/user/data/reports
RUN chown root:root /home/user/data/reports/report1.txt
RUN chown root:root /home/user/data/reports/report2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

