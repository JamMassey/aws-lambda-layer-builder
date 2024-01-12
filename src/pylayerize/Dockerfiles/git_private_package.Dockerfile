ARG RUNTIME

FROM public.ecr.aws/sam/build-${RUNTIME}

ARG RUNTIME
   
RUN mkdir -p python/lib/${RUNTIME}/site-packages 

ARG PACKAGE
ARG OUTPUT_NAME
ARG GIT_USERNAME
ARG GIT_PASSWORD
RUN git config --global credential.helper "!f() { echo username=$GIT_USERNAME; echo password=$GIT_PASSWORD; }; f"


RUN pip3 install ${PACKAGE} -t python/lib/${RUNTIME}/site-packages

RUN chmod -R 755 python/lib/${RUNTIME}/site-packages \ 
    && zip -r ${OUTPUT_NAME}.zip python/lib/${RUNTIME}/site-packages


CMD ["sleep","1"]