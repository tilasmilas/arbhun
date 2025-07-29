import structlog, sys, logging
from structlog.stdlib import LoggerFactory

logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)
structlog.configure(
    logger_factory=LoggerFactory(),
    processors=[structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.JSONRenderer()]
)
log = structlog.get_logger()
