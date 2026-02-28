FROM unix101-base:latest

USER root
RUN printf '#include <stdio.h>\nint main() { return 0; }\n' > /home/user/gamma.c
RUN printf 'void func() {}\n' > /home/user/delta.c
RUN ar rcs /home/user/libstuff.a /home/user/gamma.c /home/user/delta.c
RUN rm /home/user/gamma.c /home/user/delta.c
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

