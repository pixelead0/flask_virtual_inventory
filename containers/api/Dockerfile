FROM python:3.8
RUN mkdir /api
WORKDIR /api

EXPOSE 5000

COPY ./containers/api/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./containers/api/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
CMD ["sh entrypoint.sh"]
