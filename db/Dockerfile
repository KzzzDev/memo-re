FROM mysql:8.0

ENV MYSQL_DATABASE=django \
    MYSQL_USER=django \
    MYSQL_PASSWORD=password \
    MYSQL_ROOT_PASSWORD=password \
    TZ=Asia/Tokyo

COPY ./my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf