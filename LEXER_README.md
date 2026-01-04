# CEC Lexer - The Lexer That Feels

A Python implementation of an emotional tokenizer for Chronolexical Emoji Calculus (CEC).

## Features

✅ **Complete EBNF Tokenization**: Tokenizes all emoji operators, delimiters, and identifiers according to the CEC language specification

✅ **Emoji Variable Names**: Supports arbitrary emoji sequences as variable names using Unicode category detection

✅ **Emotional Resonance**: Each token carries an emotional resonance value
- Operators have baseline resonance values (💕 = 0.8, 💔 = -0.3, etc.)
- Emotional contagion propagates resonance to adjacent tokens
- Resonance decays and blends as tokens are processed

✅ **Temporal Whitespace Detection**:
- `\n` (newline) - Advances time by 1 unit
- `    ` (4 spaces) - Shifts dimension by 10 units
- ` ` (single space) - Micro-reversal, decreases time by 1 unit

✅ **Temporal Reversal Mode**: Read files backwards (line order reversed) while tokenizing forwards, resolving the temporal contradiction inherent in CEC

✅ **Graceful Error Handling**: Malformed input emits 💥 Reality Fracture tokens instead of raising exceptions (reality is negotiable!)

✅ **Vibe Check**: `--vibe-check` flag analyzes the overall emotional trajectory of the token stream

## Installation

No installation required! Just Python 3.6+ with standard library.

```bash
# Make the lexer executable
chmod +x cec_lexer.py
```

## Usage

### Basic Tokenization

```bash
# Tokenize a CEC file and show all tokens
python3 cec_lexer.py your_program.cec

# Or read from stdin
cat your_program.cec | python3 cec_lexer.py
```

### Vibe Check Mode

```bash
# Analyze the emotional trajectory
python3 cec_lexer.py your_program.cec --vibe-check

# Show both tokens and vibe check
python3 cec_lexer.py your_program.cec --show-tokens --vibe-check
```

### Temporal Reversal Mode

```bash
# Read file backwards (for temporal reversal execution model)
python3 cec_lexer.py your_program.cec --backwards
```

## Examples

### Example 1: Basic Tokenization

```bash
$ python3 cec_lexer.py battle_simulator.cec --show-tokens | head -10
Token(TIMELINE_BEGIN, '⏰BEGIN⏰', pos=0, resonance=0.00, temporal=0)
Token(MICRO_REVERSAL, ' ', pos=7, resonance=0.00, temporal=-1)
Token(TEMPORAL_SIG, '⏳', pos=8, resonance=0.00, temporal=-1)
Token(NUMBER, '9876543210', pos=9, resonance=0.00, temporal=-1)
...
```

### Example 2: Vibe Check

```bash
$ python3 cec_lexer.py battle_simulator.cec --vibe-check

==================================================
🌈 VIBE CHECK - Emotional Trajectory Analysis 🌈
==================================================
📊 Average Resonance: -0.032
⬆️  Peak Emotion:      +1.000
⬇️  Valley Emotion:    -1.000
📏 Emotional Range:   2.000
📈 Trajectory:        stable →
⏰ Temporal Span:     50 units
==================================================
😐 Overall vibe: Neutral - Balanced emotions
==================================================
```

## Token Structure

Each token is a dataclass with the following properties:

```python
@dataclass
class Token:
    type: TokenType           # Type of token (operator, identifier, etc.)
    value: str                # Actual text value
    position: int             # Character position in source
    emotional_resonance: float # Emotional intensity (-1.0 to 1.0)
    temporal_offset: int      # Cumulative temporal dimension offset
```

## Emotional Resonance Baselines

| Operator | Resonance | Meaning |
|----------|-----------|---------|
| 💕 | +0.8 | Love (addition) |
| 💔 | -0.3 | Heartbreak (subtraction) |
| 🔥 | +0.7 | Passion (multiplication) |
| 💧 | -0.2 | Tears (division) |
| ⚡ | +0.9 | Excitement (exponentiation) |
| 🌙 | -0.1 | Darkness (modulo) |
| 😊 | +0.7 | Happy |
| 😢 | -0.5 | Sad |
| 😡 | -0.6 | Angry |
| 😱 | -0.8 | Scared |
| 🤔 | +0.1 | Thinking |
| 🎉 | +1.0 | Celebrate |
| 🕳️ | -1.0 | Void (dark) |
| 💥 | -0.9 | Reality Fracture (error) |

## Emotional Contagion

Emotional resonance propagates through the token stream:

1. When an operator with strong resonance is encountered, it sets the emotional baseline
2. Subsequent tokens receive a fraction of the previous resonance
3. Resonance decays over time (multiplied by 0.7 for most tokens)
4. Number tokens receive 10% of previous resonance
5. String tokens receive 20% of previous resonance
6. Emoji variables receive 30% of previous resonance

This creates natural emotional "waves" through the code.

## Temporal Whitespace

CEC treats different types of whitespace as temporal operations:

- **Newline (`\n`)**: Moves forward in time (+1 temporal unit)
- **Temporal Tab (4 spaces)**: Shifts into a parallel dimension (+10 temporal units)
- **Micro-Reversal (single space)**: Backwards temporal adjustment (-1 temporal unit)

The `temporal_offset` property on each token tracks the cumulative effect of these operations.

## Testing

Run the test suite:

```bash
python3 test_cec_lexer.py
```

Tests include:
- Basic operator tokenization
- Emotional resonance tracking
- Emotional contagion propagation
- Number and string literals
- Emoji variable names
- Temporal whitespace detection
- Timeline markers
- Comment handling
- Malformed input (reality fractures)
- Backwards reading
- Vibe check calculations
- Complex program tokenization
- Quantum operators

## Python API

Use the lexer in your own code:

```python
from cec_lexer import CECLexer, calculate_vibe

# Create lexer
source = "💕 💔 🔥"
lexer = CECLexer(source)

# Tokenize (returns generator)
for token in lexer.tokenize():
    print(token)

# Or collect all tokens
tokens = list(lexer.tokenize())

# Calculate emotional trajectory
vibe = calculate_vibe(tokens)
print(f"Average resonance: {vibe['average_resonance']}")
```

## Implementation Details

### Emoji Detection

The lexer uses Unicode category detection to identify emoji:
- Categories: `So` (Other Symbol), `Sm` (Math Symbol), `Sk` (Modifier Symbol)
- Common emoji ranges: U+1F300-U+1F9FF, U+2600-U+26FF, etc.
- Handles variation selectors (e.g., ️) properly

### Backwards Reading

When `read_backwards=True`:
- Lines are reversed in order
- Each line's content remains forward
- Tokenization proceeds normally on the reversed text
- This resolves the temporal contradiction: file is read backwards, but tokens are generated forwards

### Reality Fractures

Instead of raising exceptions, the lexer emits special `REALITY_FRACTURE` tokens for:
- Unknown characters
- Unclosed strings
- Unclosed comments
- Other malformed input

This allows the lexer to continue processing and report multiple errors.

## License

This implementation is part of the Chronolexical Emoji Calculus project. See LICENSE file for details.

## Philosophy

> "In the beginning was the end, and the end was bizarre, and the bizarre was with emoji." - CEC 1:1

The CEC lexer embraces the absurd while maintaining computational rigor. It questions every assumption about lexical analysis:
- Why shouldn't tokens have feelings?
- Why can't whitespace be temporal?
- Why not read files backwards?
- What if errors are just alternate realities?

Welcome to emotional tokenization. **The future is behind us.** 🚀
