#!/usr/bin/env python3
"""Functions for handling data operations."""

import csv
from typing import List, Dict

def read_events_data(filename: str) -> List[Dict]:
    """Read the CSV file and return a list of event dictionaries."""
    events = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Year'] = int(row['Year'])
            row['Impact_Score'] = int(row['Impact_Score'])
            row['International_Significance'] = row['International_Significance'].lower() == 'true'
            events.append(row)
    return events

def filter_events(events: List[Dict], args) -> List[Dict]:
    """Filter events based on command line arguments."""
    from .utils import is_prime, is_divisible_by
    
    filtered_events = events.copy()
    
    if args.prime:
        filtered_events = [e for e in filtered_events if is_prime(e['Year'])]
    
    if args.divisible:
        filtered_events = [e for e in filtered_events if is_divisible_by(e['Year'], args.divisible)]
    
    if args.category:
        filtered_events = [e for e in filtered_events if e['Category'].lower() == args.category.lower()]
    
    if args.min_impact is not None:
        filtered_events = [e for e in filtered_events if e['Impact_Score'] >= args.min_impact]
    
    if args.international:
        filtered_events = [e for e in filtered_events if e['International_Significance']]
    
    return filtered_events

def format_event(event: Dict, args) -> str:
    """Format event output based on verbosity level."""
    if args.verbose:
        return (f"{event['Year']}: {event['Event']} - Category: {event['Category']}, "
                f"Impact: {event['Impact_Score']}, "
                f"International: {event['International_Significance']}")
    return f"{event['Year']}: {event['Event']}"