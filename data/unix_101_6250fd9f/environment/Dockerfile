FROM unix101-base:latest

USER root
RUN echo 'Quarterly sales report' > /home/user/report.txt
RUN groupadd -f staff
RUN chown user:user /home/user/report.txt
RUN chgrp users /home/user/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

