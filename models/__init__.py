"""
Auto reload for models
"""
from .engine.storage_engine import FileStorage
storage = FileStorage()
storage.reload()
