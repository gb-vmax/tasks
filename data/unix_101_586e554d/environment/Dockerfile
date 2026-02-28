FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN printf 'Report generated on 2024-06-01\nSummary: All systems nominal.\n' > /home/user/docs/report.txt
RUN b2sum /home/user/docs/report.txt > /home/user/docs/report.txt.b2sum
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

