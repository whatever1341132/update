#!/usr/bin/env python3
"""Tests for CLI functionality."""

import sys
import os
import unittest
import subprocess
from io import StringIO
from unittest.mock import patch

# Add the parent directory to the path so we can import our package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto_roadmap.__main__ import main


class TestCLI(unittest.TestCase):
    """Test cases for CLI functionality."""

    def test_main_no_args(self):
        """Test main function with no arguments shows help."""
        with patch('sys.argv', ['crypto_roadmap']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = main()
                self.assertEqual(result, 1)
                output = mock_stdout.getvalue()
                self.assertIn('usage:', output)
                self.assertIn('Crypto Roadmap - Mnemonic Generator', output)

    def test_generate_command(self):
        """Test generate command."""
        with patch('sys.argv', ['crypto_roadmap', 'generate']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = main()
                self.assertEqual(result, 0)
                output = mock_stdout.getvalue().strip()
                words = output.split()
                self.assertEqual(len(words), 12)  # Default is 12 words

    def test_generate_command_with_word_count(self):
        """Test generate command with specific word count."""
        with patch('sys.argv', ['crypto_roadmap', 'generate', '--words', '24']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = main()
                self.assertEqual(result, 0)
                output = mock_stdout.getvalue().strip()
                words = output.split()
                self.assertEqual(len(words), 24)

    def test_validate_command_valid(self):
        """Test validate command with valid mnemonic."""
        valid_mnemonic = ['abandon', 'ability', 'able', 'about', 'above', 'absent', 
                         'absorb', 'abstract', 'absurd', 'abuse', 'access', 'accident']
        with patch('sys.argv', ['crypto_roadmap', 'validate'] + valid_mnemonic):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = main()
                self.assertEqual(result, 0)
                output = mock_stdout.getvalue().strip()
                self.assertIn('✓ Valid mnemonic', output)

    def test_validate_command_invalid(self):
        """Test validate command with invalid mnemonic."""
        invalid_mnemonic = ['invalid', 'words', 'test']
        with patch('sys.argv', ['crypto_roadmap', 'validate'] + invalid_mnemonic):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = main()
                self.assertEqual(result, 1)
                output = mock_stdout.getvalue().strip()
                self.assertIn('✗ Invalid mnemonic', output)

    def test_seed_command_valid(self):
        """Test seed command with valid mnemonic."""
        valid_mnemonic = ['abandon', 'ability', 'able', 'about', 'above', 'absent', 
                         'absorb', 'abstract', 'absurd', 'abuse', 'access', 'accident']
        with patch('sys.argv', ['crypto_roadmap', 'seed'] + valid_mnemonic):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = main()
                self.assertEqual(result, 0)
                output = mock_stdout.getvalue().strip()
                # Should be a hex string (128 characters for 64 bytes)
                self.assertEqual(len(output), 128)
                # Check it's valid hex
                int(output, 16)

    def test_seed_command_with_passphrase(self):
        """Test seed command with passphrase."""
        valid_mnemonic = ['abandon', 'ability', 'able', 'about', 'above', 'absent', 
                         'absorb', 'abstract', 'absurd', 'abuse', 'access', 'accident']
        with patch('sys.argv', ['crypto_roadmap', 'seed', '--passphrase', 'test'] + valid_mnemonic):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = main()
                self.assertEqual(result, 0)
                output = mock_stdout.getvalue().strip()
                self.assertEqual(len(output), 128)

    def test_seed_command_invalid_mnemonic(self):
        """Test seed command with invalid mnemonic."""
        invalid_mnemonic = ['invalid', 'mnemonic']
        with patch('sys.argv', ['crypto_roadmap', 'seed'] + invalid_mnemonic):
            with patch('sys.stderr', new=StringIO()) as mock_stderr:
                result = main()
                self.assertEqual(result, 1)
                output = mock_stderr.getvalue().strip()
                self.assertIn('Error: Invalid mnemonic', output)


class TestCLIIntegration(unittest.TestCase):
    """Integration tests for CLI using subprocess."""

    def test_module_execution(self):
        """Test running the module with python -m."""
        result = subprocess.run(
            [sys.executable, '-m', 'crypto_roadmap', 'generate'],
            cwd='/home/runner/work/update/update',
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        words = result.stdout.strip().split()
        self.assertEqual(len(words), 12)

    def test_console_script(self):
        """Test the console script if available."""
        try:
            result = subprocess.run(
                ['crypto-roadmap', 'generate'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                words = result.stdout.strip().split()
                self.assertEqual(len(words), 12)
            # If script not found, that's also ok (depends on installation)
        except FileNotFoundError:
            # Console script not available in test environment
            self.skipTest("Console script not available")


if __name__ == "__main__":
    unittest.main()