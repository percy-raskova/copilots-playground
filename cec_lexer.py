#!/usr/bin/env python3
"""
Chronolexical Emoji Calculus (CEC) Lexer
An emotional tokenizer that feels your code.
"""

import sys
import argparse
import unicodedata
from dataclasses import dataclass
from typing import Generator, Optional, List
from enum import Enum


class TokenType(Enum):
    """Token types for CEC"""
    # Timeline markers
    TIMELINE_BEGIN = "⏰BEGIN⏰"
    TIMELINE_END = "⏰END⏰"
    TEMPORAL_SIG = "⏳"
    
    # Operators
    DECLARE = "⟺"
    ASSIGN = "⟸"
    MAYBE = "?"
    DEFINITELY = "!"
    
    # Emotional operators
    ADD_LOVE = "💕"
    SUB_HEARTBREAK = "💔"
    MUL_PASSION = "🔥"
    DIV_TEARS = "💧"
    EXP_EXCITEMENT = "⚡"
    MOD_DARKNESS = "🌙"
    
    # Unary operators
    NEGATE_DRAMA = "🎭"
    ABS_GLAMOUR = "🌟"
    IMAGINARY = "👻"
    FLOOR_WAVES = "🌊"
    CEIL_CLOUDS = "☁️"
    
    # Comparison
    GREATER = "👍"
    LESS = "👎"
    EQUAL = "🤝"
    EXACT_EQUAL = "💯"
    NOT_EQUAL = "🚫"
    
    # Control flow
    IF = "🤔"
    ELSE = "😮"
    ENDIF = "🤷"
    LOOP_START = "🔄"
    LOOP_END = "🛑"
    QUANTUM_LOOP_START = "🌀"
    QUANTUM_LOOP_END = "🌪️"
    LOOP_DOWN = "⤵️"
    ELEMENT_OF = "∈"
    
    # Quantum
    QUANTUM_START = "🔮"
    COLLAPSE = "🎲"
    SUPERPOSITION_OPEN = "⟨"
    SUPERPOSITION_CLOSE = "⟩"
    SUPERPOSITION_SEP = "|"
    
    # Functions
    VOID = "🕳️"
    RETURN = "🎁"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    COMMA = ","
    
    # Literals
    STRING_DELIM = "💬"
    REALITY_CHECK = "🚨"
    
    # Comments
    COMMENT_MULTI_START = "💭"
    COMMENT_SINGLE = "🗨️"
    
    # Emotional states
    HAPPY = "😊"
    SAD = "😢"
    ANGRY = "😡"
    SCARED = "😱"
    THINKING = "🤔"
    CELEBRATE = "🎉"
    
    # Data types
    NUMBER = "NUMBER"
    IMAGINARY_NUM = "IMAGINARY_NUM"
    EMOJI_VAR = "EMOJI_VAR"
    STRING = "STRING"
    
    # Whitespace
    NEWLINE = "NEWLINE"
    TEMPORAL_TAB = "TEMPORAL_TAB"
    MICRO_REVERSAL = "MICRO_REVERSAL"
    
    # Error
    REALITY_FRACTURE = "💥"
    
    # End of file
    EOF = "EOF"


@dataclass
class Token:
    """
    Token with emotional resonance and temporal properties.
    """
    type: TokenType
    value: str
    position: int  # Character position in source
    emotional_resonance: float = 0.0  # How much this token feels
    temporal_offset: int = 0  # Temporal dimension offset
    
    def __repr__(self):
        return (f"Token({self.type.name}, {repr(self.value)}, "
                f"pos={self.position}, resonance={self.emotional_resonance:.2f}, "
                f"temporal={self.temporal_offset})")


class CECLexer:
    """
    The Lexer That Feels - Emotional tokenizer for Chronolexical Emoji Calculus
    """
    
    # Emotional resonance baseline values for operators
    EMOTIONAL_BASELINES = {
        "💕": 0.8,   # Love
        "💔": -0.3,  # Heartbreak
        "🔥": 0.7,   # Passion
        "💧": -0.2,  # Tears
        "⚡": 0.9,   # Excitement
        "🌙": -0.1,  # Darkness
        "🎭": -0.4,  # Drama
        "🌟": 0.6,   # Glamour
        "👻": 0.0,   # Imaginary (neutral)
        "🌊": -0.15, # Waves
        "☁️": 0.3,   # Clouds
        "😊": 0.7,   # Happy
        "😢": -0.5,  # Sad
        "😡": -0.6,  # Angry
        "😱": -0.8,  # Scared
        "🤔": 0.1,   # Thinking
        "🎉": 1.0,   # Celebrate
        "🔮": 0.5,   # Quantum (mysterious)
        "🎲": 0.4,   # Dice (exciting)
        "🕳️": -1.0,  # Void (dark)
        "💥": -0.9,  # Reality fracture (catastrophic)
    }
    
    # Multi-character operators that need special handling
    MULTI_CHAR_OPERATORS = {
        "⏰BEGIN⏰": TokenType.TIMELINE_BEGIN,
        "⏰END⏰": TokenType.TIMELINE_END,
        "☁️": TokenType.CEIL_CLOUDS,
        "🕳️": TokenType.VOID,
        "🗨️": TokenType.COMMENT_SINGLE,
        "🌪️": TokenType.QUANTUM_LOOP_END,
        "⤵️": TokenType.LOOP_DOWN,
    }
    
    # Single-character operators
    SINGLE_CHAR_OPERATORS = {
        "⏳": TokenType.TEMPORAL_SIG,
        "⟺": TokenType.DECLARE,
        "⟸": TokenType.ASSIGN,
        "?": TokenType.MAYBE,
        "!": TokenType.DEFINITELY,
        "💕": TokenType.ADD_LOVE,
        "💔": TokenType.SUB_HEARTBREAK,
        "🔥": TokenType.MUL_PASSION,
        "💧": TokenType.DIV_TEARS,
        "⚡": TokenType.EXP_EXCITEMENT,
        "🌙": TokenType.MOD_DARKNESS,
        "🎭": TokenType.NEGATE_DRAMA,
        "🌟": TokenType.ABS_GLAMOUR,
        "👻": TokenType.IMAGINARY,
        "🌊": TokenType.FLOOR_WAVES,
        "👍": TokenType.GREATER,
        "👎": TokenType.LESS,
        "🤝": TokenType.EQUAL,
        "💯": TokenType.EXACT_EQUAL,
        "🚫": TokenType.NOT_EQUAL,
        "🤔": TokenType.IF,
        "😮": TokenType.ELSE,
        "🤷": TokenType.ENDIF,
        "🔄": TokenType.LOOP_START,
        "🛑": TokenType.LOOP_END,
        "🌀": TokenType.QUANTUM_LOOP_START,
        "∈": TokenType.ELEMENT_OF,
        "🔮": TokenType.QUANTUM_START,
        "🎲": TokenType.COLLAPSE,
        "⟨": TokenType.SUPERPOSITION_OPEN,
        "⟩": TokenType.SUPERPOSITION_CLOSE,
        "|": TokenType.SUPERPOSITION_SEP,
        "🎁": TokenType.RETURN,
        "(": TokenType.LPAREN,
        ")": TokenType.RPAREN,
        "{": TokenType.LBRACE,
        "}": TokenType.RBRACE,
        ",": TokenType.COMMA,
        "💬": TokenType.STRING_DELIM,
        "🚨": TokenType.REALITY_CHECK,
        "💭": TokenType.COMMENT_MULTI_START,
        "😊": TokenType.HAPPY,
        "😢": TokenType.SAD,
        "😡": TokenType.ANGRY,
        "😱": TokenType.SCARED,
        "🎉": TokenType.CELEBRATE,
        "💥": TokenType.REALITY_FRACTURE,
    }
    
    def __init__(self, source: str, read_backwards: bool = False):
        """
        Initialize the lexer.
        
        Args:
            source: The source code to tokenize
            read_backwards: If True, read file backwards but tokenize forwards
                          (resolving the temporal contradiction)
        """
        if read_backwards:
            # Read backwards: reverse the lines but keep each line's content forward
            lines = source.split('\n')
            lines.reverse()
            self.source = '\n'.join(lines)
        else:
            self.source = source
        
        self.pos = 0
        self.line = 1
        self.column = 1
        self.temporal_offset = 0  # Track temporal dimension shifts
        self.previous_resonance = 0.0  # For emotional contagion
        
    def is_emoji(self, char: str) -> bool:
        """
        Check if a character is an emoji using Unicode categories.
        """
        if not char:
            return False
        
        category = unicodedata.category(char)
        # So = Other Symbol, Sm = Math Symbol, Sk = Modifier Symbol
        if category in ['So', 'Sm', 'Sk']:
            return True
        
        # Check common emoji ranges
        code = ord(char)
        if 0x1F300 <= code <= 0x1F9FF:  # Emoticons, symbols, pictographs
            return True
        if 0x2600 <= code <= 0x26FF:    # Miscellaneous symbols
            return True
        if 0x2700 <= code <= 0x27BF:    # Dingbats
            return True
        if 0xFE00 <= code <= 0xFE0F:    # Variation selectors
            return True
        if 0x1F600 <= code <= 0x1F64F:  # Emoticons
            return True
        
        return False
    
    def peek(self, offset: int = 0) -> Optional[str]:
        """Peek at character at current position + offset."""
        pos = self.pos + offset
        if pos < len(self.source):
            return self.source[pos]
        return None
    
    def advance(self) -> Optional[str]:
        """Advance position and return current character."""
        if self.pos >= len(self.source):
            return None
        
        char = self.source[self.pos]
        self.pos += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        return char
    
    def skip_whitespace(self):
        """Skip regular whitespace (not temporal whitespace)."""
        while self.peek() and self.peek() in [' ', '\t', '\r', '\n']:
            # We track these specially, so break on them for proper handling
            if self.peek() == '\n':
                break
            if self.peek() == ' ':
                # Check if it's 4 spaces (temporal tab) or single space (micro-reversal)
                if (self.peek(0) == ' ' and self.peek(1) == ' ' and 
                    self.peek(2) == ' ' and self.peek(3) == ' '):
                    break
                # Single space is also special
                break
            self.advance()
    
    def read_number(self) -> Token:
        """Read a number literal (including imaginary numbers)."""
        start_pos = self.pos
        num_str = ""
        
        # Optional negative sign
        if self.peek() == '-':
            num_str += self.advance()
        
        # Read digits
        while self.peek() and self.peek().isdigit():
            num_str += self.advance()
        
        # Decimal point
        if self.peek() == '.':
            num_str += self.advance()
            while self.peek() and self.peek().isdigit():
                num_str += self.advance()
        
        # Imaginary marker
        is_imaginary = False
        if self.peek() == 'i':
            num_str += self.advance()
            is_imaginary = True
        
        token_type = TokenType.IMAGINARY_NUM if is_imaginary else TokenType.NUMBER
        return Token(token_type, num_str, start_pos, self.previous_resonance * 0.1, self.temporal_offset)
    
    def read_string(self) -> Token:
        """Read a string literal enclosed in 💬."""
        start_pos = self.pos
        self.advance()  # Skip opening 💬
        
        string_content = ""
        while self.peek() and self.peek() != "💬":
            string_content += self.advance()
        
        if self.peek() == "💬":
            self.advance()  # Skip closing 💬
        else:
            # Malformed string - emit reality fracture
            return Token(TokenType.REALITY_FRACTURE, 
                        f"Unclosed string: {string_content}", 
                        start_pos, -0.9, self.temporal_offset)
        
        return Token(TokenType.STRING, string_content, start_pos, 
                    self.previous_resonance * 0.2, self.temporal_offset)
    
    def read_emoji_variable(self) -> Token:
        """Read an emoji variable name (arbitrary emoji sequence)."""
        start_pos = self.pos
        emoji_str = ""
        
        while self.peek() and self.is_emoji(self.peek()):
            # Skip if it's a known operator
            if self.peek() in self.SINGLE_CHAR_OPERATORS:
                break
            # Check for multi-char operators
            is_operator = False
            for op in self.MULTI_CHAR_OPERATORS:
                if self.source[self.pos:self.pos + len(op)] == op:
                    is_operator = True
                    break
            if is_operator:
                break
            
            emoji_str += self.advance()
        
        if not emoji_str:
            return None
        
        # Apply emotional contagion from previous token
        resonance = self.previous_resonance * 0.3
        return Token(TokenType.EMOJI_VAR, emoji_str, start_pos, resonance, self.temporal_offset)
    
    def read_comment_single_line(self) -> Token:
        """Read a single-line comment starting with 🗨️."""
        start_pos = self.pos
        self.advance()  # Skip 🗨️
        
        comment = ""
        while self.peek() and self.peek() != '\n':
            comment += self.advance()
        
        # Comments don't produce tokens (they're skipped)
        return None
    
    def read_comment_multi_line(self) -> Token:
        """Read a multi-line comment enclosed in 💭."""
        start_pos = self.pos
        self.advance()  # Skip opening 💭
        
        comment = ""
        while self.peek() and self.peek() != "💭":
            comment += self.advance()
        
        if self.peek() == "💭":
            self.advance()  # Skip closing 💭
        else:
            # Malformed comment - emit reality fracture
            return Token(TokenType.REALITY_FRACTURE, 
                        f"Unclosed comment: {comment[:20]}...", 
                        start_pos, -0.9, self.temporal_offset)
        
        # Comments don't produce tokens (they're skipped)
        return None
    
    def apply_emotional_contagion(self, token: Token):
        """
        Apply emotional contagion - propagate resonance to future tokens.
        """
        if token.type in [TokenType.REALITY_FRACTURE]:
            # Strong negative emotions propagate
            self.previous_resonance = token.emotional_resonance
        elif token.emotional_resonance != 0.0:
            # Decay previous resonance and add new
            self.previous_resonance = (self.previous_resonance * 0.5 + 
                                      token.emotional_resonance * 0.5)
        else:
            # Decay previous resonance
            self.previous_resonance *= 0.7
    
    def tokenize(self) -> Generator[Token, None, None]:
        """
        Generate tokens from the source code.
        Yields Token dataclasses with emotional resonance and temporal properties.
        """
        while self.pos < len(self.source):
            # Handle temporal whitespace
            if self.peek() == '\n':
                # Newline advances time
                pos = self.pos
                self.advance()
                self.temporal_offset += 1
                token = Token(TokenType.NEWLINE, "\\n", pos, 0.0, self.temporal_offset)
                self.apply_emotional_contagion(token)
                yield token
                continue
            
            # Check for 4 spaces (temporal tab - shift dimension)
            if (self.peek(0) == ' ' and self.peek(1) == ' ' and 
                self.peek(2) == ' ' and self.peek(3) == ' '):
                pos = self.pos
                for _ in range(4):
                    self.advance()
                self.temporal_offset += 10  # Dimension shift is bigger
                token = Token(TokenType.TEMPORAL_TAB, "    ", pos, 0.0, self.temporal_offset)
                self.apply_emotional_contagion(token)
                yield token
                continue
            
            # Single space is micro-reversal
            if self.peek() == ' ':
                pos = self.pos
                self.advance()
                self.temporal_offset -= 1  # Reversal
                token = Token(TokenType.MICRO_REVERSAL, " ", pos, 0.0, self.temporal_offset)
                self.apply_emotional_contagion(token)
                yield token
                continue
            
            # Skip other whitespace
            if self.peek() in ['\t', '\r']:
                self.advance()
                continue
            
            # Check for multi-character operators
            matched = False
            for op_str, token_type in self.MULTI_CHAR_OPERATORS.items():
                if self.source[self.pos:self.pos + len(op_str)] == op_str:
                    pos = self.pos
                    
                    # Special handling for comments
                    if token_type == TokenType.COMMENT_SINGLE:
                        for _ in range(len(op_str)):
                            self.advance()
                        self.read_comment_single_line()
                        matched = True
                        break
                    
                    # Normal operator
                    for _ in range(len(op_str)):
                        self.advance()
                    resonance = self.EMOTIONAL_BASELINES.get(op_str, 0.0)
                    token = Token(token_type, op_str, pos, resonance, self.temporal_offset)
                    self.apply_emotional_contagion(token)
                    yield token
                    matched = True
                    break
            
            if matched:
                continue
            
            # Multi-line comments
            if self.peek() == "💭":
                comment_token = self.read_comment_multi_line()
                if comment_token:  # Reality fracture
                    self.apply_emotional_contagion(comment_token)
                    yield comment_token
                continue
            
            # Strings
            if self.peek() == "💬":
                token = self.read_string()
                self.apply_emotional_contagion(token)
                yield token
                continue
            
            # Numbers
            if self.peek() and (self.peek().isdigit() or 
                              (self.peek() == '-' and self.peek(1) and self.peek(1).isdigit())):
                token = self.read_number()
                self.apply_emotional_contagion(token)
                yield token
                continue
            
            # Single-character operators
            if self.peek() in self.SINGLE_CHAR_OPERATORS:
                char = self.peek()
                pos = self.pos
                self.advance()
                token_type = self.SINGLE_CHAR_OPERATORS[char]
                resonance = self.EMOTIONAL_BASELINES.get(char, 0.0)
                token = Token(token_type, char, pos, resonance, self.temporal_offset)
                self.apply_emotional_contagion(token)
                yield token
                continue
            
            # Emoji variables (must come after checking for emoji operators)
            if self.is_emoji(self.peek()):
                token = self.read_emoji_variable()
                if token:
                    self.apply_emotional_contagion(token)
                    yield token
                    continue
            
            # Unknown character - emit reality fracture instead of error
            char = self.peek()
            pos = self.pos
            self.advance()
            token = Token(TokenType.REALITY_FRACTURE, 
                         f"Unknown character: {char}", 
                         pos, -0.9, self.temporal_offset)
            self.apply_emotional_contagion(token)
            yield token
        
        # End of file
        yield Token(TokenType.EOF, "", self.pos, 0.0, self.temporal_offset)


def calculate_vibe(tokens: List[Token]) -> dict:
    """
    Calculate the emotional trajectory of a token stream.
    """
    if not tokens:
        return {
            "average_resonance": 0.0,
            "peak_emotion": 0.0,
            "valley_emotion": 0.0,
            "emotional_range": 0.0,
            "trajectory": "neutral",
            "temporal_span": 0,
        }
    
    resonances = [t.emotional_resonance for t in tokens if t.type != TokenType.EOF]
    
    if not resonances:
        resonances = [0.0]
    
    avg = sum(resonances) / len(resonances)
    peak = max(resonances)
    valley = min(resonances)
    emotional_range = peak - valley
    
    # Determine trajectory
    if len(resonances) > 1:
        first_half = sum(resonances[:len(resonances)//2]) / (len(resonances)//2)
        second_half = sum(resonances[len(resonances)//2:]) / (len(resonances) - len(resonances)//2)
        
        if second_half > first_half + 0.1:
            trajectory = "ascending ↗️"
        elif second_half < first_half - 0.1:
            trajectory = "descending ↘️"
        else:
            trajectory = "stable →"
    else:
        trajectory = "static"
    
    temporal_span = tokens[-1].temporal_offset if tokens else 0
    
    return {
        "average_resonance": avg,
        "peak_emotion": peak,
        "valley_emotion": valley,
        "emotional_range": emotional_range,
        "trajectory": trajectory,
        "temporal_span": temporal_span,
    }


def print_vibe_check(vibe: dict):
    """Print a nice vibe check report."""
    print("\n" + "="*50)
    print("🌈 VIBE CHECK - Emotional Trajectory Analysis 🌈")
    print("="*50)
    print(f"📊 Average Resonance: {vibe['average_resonance']:+.3f}")
    print(f"⬆️  Peak Emotion:      {vibe['peak_emotion']:+.3f}")
    print(f"⬇️  Valley Emotion:    {vibe['valley_emotion']:+.3f}")
    print(f"📏 Emotional Range:   {vibe['emotional_range']:.3f}")
    print(f"📈 Trajectory:        {vibe['trajectory']}")
    print(f"⏰ Temporal Span:     {vibe['temporal_span']} units")
    print("="*50)
    
    # Vibe interpretation
    avg = vibe['average_resonance']
    if avg > 0.5:
        print("💖 Overall vibe: VERY POSITIVE - This code is in love!")
    elif avg > 0.2:
        print("😊 Overall vibe: Positive - Happy little tokens")
    elif avg > -0.2:
        print("😐 Overall vibe: Neutral - Balanced emotions")
    elif avg > -0.5:
        print("😢 Overall vibe: Negative - Some sadness here")
    else:
        print("💔 Overall vibe: VERY NEGATIVE - Dark times ahead")
    print("="*50 + "\n")


def main():
    """Main entry point for the lexer."""
    parser = argparse.ArgumentParser(
        description="Chronolexical Emoji Calculus (CEC) Lexer - The Lexer That Feels"
    )
    parser.add_argument("file", nargs="?", help="CEC source file to tokenize")
    parser.add_argument("--vibe-check", action="store_true", 
                       help="Print overall emotional trajectory of the token stream")
    parser.add_argument("--backwards", action="store_true",
                       help="Read file backwards (temporal reversal mode)")
    parser.add_argument("--show-tokens", action="store_true",
                       help="Show all tokens (default if no --vibe-check)")
    
    args = parser.parse_args()
    
    # Read source
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                source = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Read from stdin
        source = sys.stdin.read()
    
    # Create lexer and tokenize
    lexer = CECLexer(source, read_backwards=args.backwards)
    tokens = list(lexer.tokenize())
    
    # Show tokens if requested or if vibe-check not requested
    if args.show_tokens or not args.vibe_check:
        for token in tokens:
            if token.type not in [TokenType.EOF]:
                print(token)
    
    # Vibe check if requested
    if args.vibe_check:
        vibe = calculate_vibe(tokens)
        print_vibe_check(vibe)


if __name__ == "__main__":
    main()
