FROM unix101-base:latest

USER root
RUN echo 'Monthly sales report' > /home/user/report.txt
RUN echo 'id,amount' > /home/user/data.csv
RUN echo '1,100' >> /home/user/data.csv
RUN printf "/home/user/report.txt\n/home/user/data.csv\n" > /home/user/filelist.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

