#!/usr/bin/env python3
"""Command-line interface for crypto_roadmap package."""

import argparse
import sys
from .mnemonic import MnemonicGenerator


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Crypto Roadmap - Mnemonic Generator",
        prog="crypto_roadmap"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Generate mnemonic command
    generate_parser = subparsers.add_parser(
        'generate', 
        help='Generate a new mnemonic phrase'
    )
    generate_parser.add_argument(
        '--words', '-w',
        type=int,
        default=12,
        choices=[12, 15, 18, 21, 24],
        help='Number of words in the mnemonic (default: 12)'
    )
    
    # Validate mnemonic command
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate a mnemonic phrase'
    )
    validate_parser.add_argument(
        'mnemonic',
        nargs='+',
        help='Mnemonic phrase to validate'
    )
    
    # Convert to seed command
    seed_parser = subparsers.add_parser(
        'seed',
        help='Convert mnemonic to seed'
    )
    seed_parser.add_argument(
        'mnemonic',
        nargs='+',
        help='Mnemonic phrase to convert'
    )
    seed_parser.add_argument(
        '--passphrase', '-p',
        default='',
        help='Optional passphrase for seed generation'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Initialize generator
    generator = MnemonicGenerator()
    
    try:
        if args.command == 'generate':
            mnemonic = generator.generate_mnemonic(args.words)
            print(mnemonic)
            
        elif args.command == 'validate':
            mnemonic = ' '.join(args.mnemonic)
            is_valid = generator.validate_mnemonic(mnemonic)
            if is_valid:
                print("✓ Valid mnemonic")
                return 0
            else:
                print("✗ Invalid mnemonic")
                return 1
                
        elif args.command == 'seed':
            mnemonic = ' '.join(args.mnemonic)
            if not generator.validate_mnemonic(mnemonic):
                print("Error: Invalid mnemonic", file=sys.stderr)
                return 1
            seed = generator.mnemonic_to_seed(mnemonic, args.passphrase)
            print(seed)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    return 0


if __name__ == '__main__':
    sys.exit(main())