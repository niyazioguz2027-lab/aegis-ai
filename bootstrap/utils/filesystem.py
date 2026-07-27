"""Utility functions for file operations."""

from pathlib import Path
from typing import Generator


def ensure_dir(path: Path) -> Path:
    """Create directory and return the path.
    
    Args:
        path: Directory path to create
        
    Returns:
        The created directory path
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_file(path: Path, content: str) -> None:
    """Write content to file.
    
    Args:
        path: File path
        content: File content
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read_file(path: Path) -> str:
    """Read file content.
    
    Args:
        path: File path
        
    Returns:
        File content
    """
    return path.read_text(encoding="utf-8")


def file_exists(path: Path) -> bool:
    """Check if file exists.
    
    Args:
        path: File path
        
    Returns:
        True if file exists
    """
    return path.exists()


def walk_files(root: Path, pattern: str = "*") -> Generator[Path, None, None]:
    """Walk files recursively.
    
    Args:
        root: Root directory
        pattern: File pattern to match
        
    Yields:
        File paths matching pattern
    """
    for item in root.glob(f"**/{pattern}"):
        if item.is_file():
            yield item
