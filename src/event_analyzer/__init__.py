"""Event Analyzer package for historical events in India."""
from .utils import is_prime, is_divisible_by
from .data_handler import read_events_data, filter_events, format_event

__all__ = [
    'is_prime',
    'is_divisible_by',
    'read_events_data',
    'filter_events',
    'format_event'
]