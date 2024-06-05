#docker build -t mam10eks/github-page-tutorial:0.0.2 .
# This image already contains all dependencies: ir_datasets, tira, vuetify, etc.
FROM webis/tira-application:basis-0.0.96


ENV PATH=${PATH}:/usr/local/lib/node_modules/.bin/

ADD ui /ui

RUN cd /ui \
	&& rm node_modules \
	&& npm install \
	&& rm -R /usr/local/lib/node_modules \
	&& mv node_modules /usr/local/lib/node_modules \
	&& rm -Rf /ui


