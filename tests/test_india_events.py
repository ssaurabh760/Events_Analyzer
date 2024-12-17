#!/usr/bin/env python3
import unittest
import tempfile
import os
import logging
from datetime import datetime
from pathlib import Path
from src.event_analyzer.utils import is_prime, is_divisible_by
from src.event_analyzer.data_handler import read_events_data, filter_events, format_event

# Create logs directory if it doesn't exist
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / f'test_execution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TestIndiaEventsAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("Starting test suite execution")
        # Create a temporary CSV file for testing
        cls.test_data = '''Year,Event,Category,Impact_Score,International_Significance
1971,Test Event 1,Military,8,True
1972,Test Event 2,Political,7,False
1973,Test Event 3,Economic,9,True
1974,Test Event 4,Social,6,False
1975,Test Event 5,Military,10,True'''
        
        try:
            cls.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
            cls.temp_file.write(cls.test_data)
            cls.temp_file.close()
            logger.info(f"Created temporary test file: {cls.temp_file.name}")
        except Exception as e:
            logger.error(f"Failed to create temporary test file: {str(e)}")
            raise
    
    @classmethod
    def tearDownClass(cls):
        try:
            os.unlink(cls.temp_file.name)
            logger.info(f"Removed temporary test file: {cls.temp_file.name}")
        except Exception as e:
            logger.error(f"Failed to remove temporary test file: {str(e)}")
        logger.info("Completed test suite execution")

    def setUp(self):
        logger.info(f"\nStarting test: {self._testMethodName}")

    def tearDown(self):
        logger.info(f"Completed test: {self._testMethodName}")

    def test_is_prime(self):
        logger.info("Testing prime number functionality")
        test_cases = [
            (1973, True, "Testing prime year"),
            (1974, False, "Testing non-prime year"),
            (1, False, "Testing edge case 1"),
            (2, True, "Testing edge case 2"),
            (11, True, "Testing small prime")
        ]
        
        for number, expected, message in test_cases:
            logger.debug(f"{message}: testing {number}")
            try:
                if expected:
                    self.assertTrue(is_prime(number))
                    logger.info(f"✓ {number} correctly identified as prime")
                else:
                    self.assertFalse(is_prime(number))
                    logger.info(f"✓ {number} correctly identified as non-prime")
            except AssertionError:
                logger.error(f"✗ Failed prime test for {number}")
                raise

    def test_is_divisible_by(self):
        logger.info("Testing divisibility functionality")
        test_cases = [
            (1972, 2, True, "Testing even number"),
            (1973, 2, False, "Testing odd number"),
            (1975, 5, True, "Testing divisibility by 5"),
            (1973, 3, False, "Testing non-divisibility by 3")
        ]
        
        for number, divisor, expected, message in test_cases:
            logger.debug(f"{message}: testing {number} divisible by {divisor}")
            try:
                if expected:
                    self.assertTrue(is_divisible_by(number, divisor))
                    logger.info(f"✓ {number} correctly identified as divisible by {divisor}")
                else:
                    self.assertFalse(is_divisible_by(number, divisor))
                    logger.info(f"✓ {number} correctly identified as not divisible by {divisor}")
            except AssertionError:
                logger.error(f"✗ Failed divisibility test for {number} by {divisor}")
                raise

    def test_read_events_data(self):
        logger.info("Testing event data reading functionality")
        try:
            events = read_events_data(self.temp_file.name)
            self.assertEqual(len(events), 5)
            logger.info("✓ Correct number of events read")
            
            # Test first event details
            self.assertEqual(events[0]['Year'], 1971)
            self.assertEqual(events[0]['Category'], 'Military')
            self.assertTrue(events[0]['International_Significance'])
            self.assertEqual(events[0]['Impact_Score'], 8)
            logger.info("✓ First event data correctly parsed")
        except Exception as e:
            logger.error(f"Failed to read events data: {str(e)}")
            raise

    def test_filter_events(self):
        logger.info("Testing event filtering functionality")
        events = read_events_data(self.temp_file.name)
        
        class Args:
            prime = True
            divisible = None
            category = None
            min_impact = None
            international = False

        # Test different filters
        filter_tests = [
            ("Prime years", {"prime": True}, 1),
            ("Divisible by 2", {"prime": False, "divisible": 2}, 2),
            ("Military category", {"divisible": None, "category": "Military"}, 2),
            ("High impact", {"category": None, "min_impact": 9}, 2),
            ("International", {"min_impact": None, "international": True}, 3)
        ]

        for test_name, filter_args, expected_count in filter_tests:
            logger.info(f"Testing filter: {test_name}")
            for key, value in filter_args.items():
                setattr(Args, key, value)
            
            try:
                filtered = filter_events(events, Args)
                self.assertEqual(len(filtered), expected_count)
                logger.info(f"✓ {test_name} filter returned correct number of events: {expected_count}")
            except AssertionError:
                logger.error(f"✗ {test_name} filter returned wrong number of events")
                raise

    def test_format_event(self):
        logger.info("Testing event formatting functionality")
        event = {
            'Year': 1971,
            'Event': 'Test Event 1',
            'Category': 'Military',
            'Impact_Score': 8,
            'International_Significance': True
        }
        
        class Args:
            verbose = False
        
        try:
            # Test normal format
            normal_output = format_event(event, Args)
            self.assertEqual(normal_output, "1971: Test Event 1")
            logger.info("✓ Normal format correct")
            
            # Test verbose format
            Args.verbose = True
            verbose_output = format_event(event, Args)
            for expected in ['Category: Military', 'Impact: 8', 'International: True']:
                self.assertIn(expected, verbose_output)
            logger.info("✓ Verbose format correct")
        except AssertionError as e:
            logger.error(f"Failed formatting test: {str(e)}")
            raise

if __name__ == '__main__':
    logger.info("=== Starting India Events Analyzer Test Suite ===")
    unittest.main(verbosity=2)