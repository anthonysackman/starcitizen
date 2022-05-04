from flask.cli import FlaskGroup

from app import app, db
import logging


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    logging.info("Creating Database...")
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
