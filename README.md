# Crypto Roadmap

A comprehensive roadmap for learning cryptocurrency, blockchain technology, and related concepts.

## Overview

This repository provides a structured learning path for understanding the cryptocurrency and blockchain ecosystem, from basic concepts to advanced topics.

## Installation

```bash
pip install .
```

## Usage

The crypto-roadmap package can be used both as a Python library and as a command-line tool.

### Command Line Interface

After installation, you can use the `crypto-roadmap` command or run the module with `python -m crypto_roadmap`:

#### Generate a mnemonic phrase
```bash
# Generate a 12-word mnemonic (default)
crypto-roadmap generate

# Generate a 24-word mnemonic
crypto-roadmap generate --words 24
```

#### Validate a mnemonic phrase
```bash
crypto-roadmap validate abandon ability able about above absent absorb abstract absurd abuse access accident
```

#### Convert mnemonic to seed
```bash
# Without passphrase
crypto-roadmap seed abandon ability able about above absent absorb abstract absurd abuse access accident

# With passphrase
crypto-roadmap seed --passphrase "my secret" abandon ability able about above absent absorb abstract absurd abuse access accident
```

### Python Library

```python
from crypto_roadmap.mnemonic import MnemonicGenerator

# Create generator
generator = MnemonicGenerator()

# Generate mnemonic
mnemonic = generator.generate_mnemonic(12)
print(mnemonic)

# Validate mnemonic
is_valid = generator.validate_mnemonic(mnemonic)
print(f"Valid: {is_valid}")

# Convert to seed
seed = generator.mnemonic_to_seed(mnemonic, passphrase="")
print(f"Seed: {seed}")
```

## Getting Started

This roadmap is designed to help both beginners and intermediate learners navigate the complex world of cryptocurrency and blockchain technology.

## Learning Path

### 1. Foundation
- Basic cryptography concepts
- Introduction to blockchain technology
- Understanding cryptocurrencies

### 2. Technical Deep Dive
- Blockchain architecture
- Consensus mechanisms
- Smart contracts

### 3. Practical Applications
- DeFi (Decentralized Finance)
- NFTs (Non-Fungible Tokens)
- Web3 development

### 4. Advanced Topics
- Layer 2 solutions
- Interoperability
- Security best practices

## Contributing

Feel free to contribute to this roadmap by opening issues or pull requests with suggestions for improvements or additional resources.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
