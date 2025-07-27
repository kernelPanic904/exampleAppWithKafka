from sqlalchemy.orm import registry

from infrastructure.models.metadata import metadata

mapper_registry = registry(metadata=metadata)
