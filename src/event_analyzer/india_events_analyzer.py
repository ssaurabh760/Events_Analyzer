#!/usr/bin/env python3
"""Main script for analyzing historical events in India."""

import argparse
import sys
from typing import List, Dict
from pathlib import Path

# Add the parent directory to sys.path to allow module imports
sys.path.append(str(Path(__file__).parent.parent))

from event_analyzer.data_handler import read_events_data, filter_events, format_event

def main():
    parser = argparse.ArgumentParser(description='Analyze historical events in India')
    parser.add_argument('file', help='CSV file containing event data')
    parser.add_argument('-p', '--prime', action='store_true',
                        help='Show only events from prime numbered years')
    parser.add_argument('-a', '--divisible', type=int,
                        help='Show only events from years divisible by this number')
    parser.add_argument('-c', '--category', type=str,
                        help='Filter events by category')
    parser.add_argument('-m', '--min-impact', type=int, choices=range(1, 11),
                        help='Show only events with at least this impact score (1-10)')
    parser.add_argument('-i', '--international', action='store_true',
                        help='Show only events with international significance')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show detailed information for each event')

    args = parser.parse_args()
    
    try:
        events = read_events_data(args.file)
        filtered_events = filter_events(events, args)
        
        if not filtered_events:
            print("No events found matching the specified criteria.")
            return
        
        for event in filtered_events:
            print(format_event(event, args))
            
    except FileNotFoundError:
        print(f"Error: Could not find file '{args.file}'")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()