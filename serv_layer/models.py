from db import db, metadata, sqlalchemy


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


class Post:

    @classmethod    
    async def get_all(self):
        query = posts.select()
        return await db.fetch_all(query)

    @classmethod
    async def get(cls, id):
        query = posts.select().where(posts.c.id == id)
        post = await db.fetch_one(query)
        return post

    @classmethod
    async def create(cls, **post):
        query = posts.insert().values(**post)
        post_id = await db.execute(query)
        return post_id

    @classmethod
    async def put(cls, id: int, **post):
        query = (
            posts
            .update()
            .where(id == posts.c.id)
            .values(post)
            .returning(posts.c.id)
        )
        return await db.execute(query=query)

    @classmethod
    async def delete(cls, id: int):
        query = posts.delete().where(id == posts.c.id)
        return await db.execute(query=query)