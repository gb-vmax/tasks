FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/reports
RUN printf 'ID\tScore\tStatus\n1\t88\tPass\n2\t75\tFail\n' > /home/user/reports/columns.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

