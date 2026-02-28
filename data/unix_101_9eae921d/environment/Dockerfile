FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs/finance
RUN mkdir -p /home/user/docs/hr
RUN echo 'Q1 summary' > /home/user/docs/report.txt
RUN echo 'Payroll' > /home/user/docs/hr/report.txt
RUN echo 'Budget' > /home/user/docs/finance/report.txt
RUN echo 'notes' > /home/user/docs/finance/notes.txt
RUN touch /home/user/report.txt
RUN updatedb --output=/var/lib/mlocate/mlocate.db --prunepaths='/tmp /var/tmp /dev /proc /sys /run' --prunefs='proc sysfs tmpfs devtmpfs devpts'
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

