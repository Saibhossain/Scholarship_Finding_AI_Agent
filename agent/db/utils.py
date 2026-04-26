def serialize_sqlalchemy(obj):
    """
    Convert SQLAlchemy model to clean dict (no _sa_instance_state)
    """
    return {
        column.name: getattr(obj, column.name)
        for column in obj.__table__.columns
    }
