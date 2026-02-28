FROM unix101-base:latest

USER root
RUN groupadd -f developers
RUN groupadd -f managers
RUN echo 'owned by managers' > /home/user/owner.txt
RUN mkdir -p /home/user/project/subdir
RUN echo 'source code' > /home/user/project/main.py
RUN echo 'test file' > /home/user/project/subdir/test.py
RUN chown user:user /home/user/owner.txt
RUN chown -R user:user /home/user/project
RUN chgrp developers /home/user/project
RUN chgrp developers /home/user/project/main.py
RUN chgrp developers /home/user/project/subdir
RUN chgrp developers /home/user/project/subdir/test.py
RUN chgrp managers /home/user/owner.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

