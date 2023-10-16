# flaskr

Simple Flask blogging application, adapted from https://flask.palletsprojects.com/en/2.3.x/tutorial/.

## Supported Databases

Database portability is provided by [SQLAlchemy](https://www.sqlalchemy.org/),
so major database engines should be supported with little to no modification.
Database backend can be configured by setting the `DATABASE_URI` environment variable.

Tested databases:
- [sqlite3](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html)
- [MySQL 8.0](https://docs.sqlalchemy.org/en/20/dialects/mysql.html) - use `pymysql` driver
