FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN printf "The woods are lovely, dark and deep\nBut I have promises to keep\nAnd miles to go before I sleep\nAnd miles to go before I sleep\nWhose woods these are I think I know.\nHis house is in the village though;\nHe will not see me stopping here\nTo watch his woods fill up with snow.\nMy little horse must think it queer\nTo stop without a farmhouse near.\n" > /home/user/docs/poem.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

