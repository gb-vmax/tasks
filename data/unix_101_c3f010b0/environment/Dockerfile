FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN bash -c 'echo "#!/bin/bash\nsleep 1000" > /home/user/fakeproc1.sh'
RUN chmod +x /home/user/fakeproc1.sh
RUN bash -c 'echo "#!/bin/bash\nsleep 1000" > /home/user/fakeproc2.sh'
RUN chmod +x /home/user/fakeproc2.sh
RUN su user -c 'nohup /home/user/fakeproc1.sh > /home/user/proc1.out 2>&1 &'
RUN su user -c 'nohup /home/user/fakeproc2.sh > /home/user/proc2.out 2>&1 &'
RUN sleep 1
RUN ps -u user -o pid=,comm= | awk '/fakeproc/ {print $1}' > /home/user/user_proc_pids.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

