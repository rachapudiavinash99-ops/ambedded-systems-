import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_alert(alert_message):
    logger.warning(f"ALERT: {alert_message}")
