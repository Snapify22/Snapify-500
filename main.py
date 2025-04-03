from app import app, socketio
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        logger.info("Starting server with eventlet WebSocket support")
        # ALWAYS serve the app on port 5000
        socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=True, log_output=True)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        sys.exit(1)