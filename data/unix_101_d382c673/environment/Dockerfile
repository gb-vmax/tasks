FROM unix101-base:latest

USER root
RUN printf "Start\nCommon\nEnd\n" > /home/user/original.txt
RUN printf "Start\nFeatureA\nEnd\n" > /home/user/featureA.txt
RUN printf "Start\nCommon\nFeatureB\nEnd\n" > /home/user/featureB.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

