"""Structured logging for bootstrap operations."""

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class StructuredLogger:
    """Structured logging with JSON output."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        """Initialize structured logger.
        
        Args:
            name: Logger name
            level: Logging level
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter("%(message)s"))
        self.logger.addHandler(handler)

    def info(self, message: str, **kwargs: Any) -> None:
        """Log info message.
        
        Args:
            message: Log message
            **kwargs: Additional context data
        """
        self._log("info", message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        """Log error message.
        
        Args:
            message: Log message
            **kwargs: Additional context data
        """
        self._log("error", message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning message.
        
        Args:
            message: Log message
            **kwargs: Additional context data
        """
        self._log("warning", message, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug message.
        
        Args:
            message: Log message
            **kwargs: Additional context data
        """
        self._log("debug", message, **kwargs)

    def _log(self, level: str, message: str, **kwargs: Any) -> None:
        """Internal log function.
        
        Args:
            level: Log level
            message: Log message
            **kwargs: Additional context data
        """
        log_entry: Dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
        }
        log_entry.update(kwargs)
        self.logger.info(json.dumps(log_entry))
