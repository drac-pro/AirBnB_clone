#!/usr/bin/python3
"""creates a unique file storage for the project(application)"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
