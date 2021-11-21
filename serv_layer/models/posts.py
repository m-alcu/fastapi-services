from db import metadata, sqlalchemy

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("body", sqlalchemy.String),
    sqlalchemy.Column("is_published", sqlalchemy.Boolean),
    sqlalchemy.Column("created", sqlalchemy.DateTime, default=sqlalchemy.sql.func.now(), nullable=False),
    sqlalchemy.Column("modified", sqlalchemy.DateTime, onupdate=sqlalchemy.sql.func.now()),
)
