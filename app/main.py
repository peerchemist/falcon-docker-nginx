
from log import logger
from conf import loglevel

import json
import falcon

engine = create_engine(
	'sqlite:///sqlite.db'
)
Base = declarative_base(engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class SQLAlchemySessionManager:
    """database handling middleware"""

    def __init__(self, Session):
        self.Session = Session

    def process_resource(self, req, resp, resource, params):
        resource.session = self.Session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            resource.session.close()


class ResponseLoggerMiddleware:
    """logging middleware"""

    def process_response(self, req, resp, resource, req_succeeded):
        if loglevel == "info":
            logger.debug('{0} {1} {2}'.format(req.method, req.relative_uri, req_succeeded))
        if loglevel == "debug":
            logger.debug('{0} {1} {2}'.format(req.method, req.relative_uri, req_succeeded))


class HelloWord:

    """Hello Word!"""

    def on_get(self, req, resp):
        
        resp.text = json.dumps("Hello World!")
        resp.status = falcon.HTTP_200  # This is the default status


app = falcon.App(cors_enable=True,
        middleware=[
        SQLAlchemySessionManager(Session),
        ResponseLoggerMiddleware(),
])

hello = HelloWord()
app.add_route('/hello', hello)
