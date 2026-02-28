FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/projects/2024
RUN echo 'Annual plan' > /home/user/Budget2024.txt
RUN echo 'Monthly' > /home/user/projects/BUDGET_report.txt
RUN echo 'Q2' > /home/user/projects/2024/budget-draft.txt
RUN echo 'Other' > /home/user/projects/2024/plan.txt
RUN echo 'Personal' > /home/user/my_budget.txt
RUN echo 'random' > /home/user/budget
RUN updatedb --output=/var/lib/mlocate/mlocate.db --prunepaths='/tmp /var/tmp /dev /proc /sys /run' --prunefs='proc sysfs tmpfs devtmpfs devpts'
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

