FROM unix101-base:latest

USER root
RUN printf "> This is a quoted paragraph that should be reformatted using crown margin.\n> Another quoted line that is part of the same paragraph.\nNormal line that should be left untouched.\n> Yet another quoted paragraph for testing.\n> Followed by its continuation.\n" > /home/user/prefix_text.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

