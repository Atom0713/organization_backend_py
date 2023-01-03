from src.models import Position


def get_all_positions():
    return [position.to_dict() for position in Position.get_all()]
