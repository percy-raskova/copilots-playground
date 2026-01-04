#!/usr/bin/env python3
"""
Tests for the CEC Lexer
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cec_lexer import CECLexer, Token, TokenType, calculate_vibe


def test_basic_operators():
    """Test tokenization of basic operators."""
    source = "💕 💔 🔥 💧"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    # Should have 4 operators + whitespace + EOF
    assert any(t.type == TokenType.ADD_LOVE for t in tokens)
    assert any(t.type == TokenType.SUB_HEARTBREAK for t in tokens)
    assert any(t.type == TokenType.MUL_PASSION for t in tokens)
    assert any(t.type == TokenType.DIV_TEARS for t in tokens)
    print("✓ test_basic_operators passed")


def test_emotional_resonance():
    """Test that operators have correct emotional resonance."""
    source = "💕 💔"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    love_token = next(t for t in tokens if t.type == TokenType.ADD_LOVE)
    heartbreak_token = next(t for t in tokens if t.type == TokenType.SUB_HEARTBREAK)
    
    assert love_token.emotional_resonance == 0.8
    assert heartbreak_token.emotional_resonance == -0.3
    print("✓ test_emotional_resonance passed")


def test_emotional_contagion():
    """Test that emotional resonance propagates to adjacent tokens."""
    source = "💕 42"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    # Find the number token
    number_token = next(t for t in tokens if t.type == TokenType.NUMBER)
    
    # Number should have some emotional resonance from the love operator
    # (0.8 * 0.5 * 0.1 from previous resonance decay and number propagation)
    assert number_token.emotional_resonance > 0.0
    print("✓ test_emotional_contagion passed")


def test_numbers():
    """Test number tokenization."""
    source = "42 3.14 -5 42i"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    number_tokens = [t for t in tokens if t.type in [TokenType.NUMBER, TokenType.IMAGINARY_NUM]]
    
    assert len(number_tokens) == 4
    assert any(t.value == "42" for t in number_tokens)
    assert any(t.value == "3.14" for t in number_tokens)
    assert any(t.value == "-5" for t in number_tokens)
    assert any(t.value == "42i" and t.type == TokenType.IMAGINARY_NUM for t in number_tokens)
    print("✓ test_numbers passed")


def test_strings():
    """Test string tokenization."""
    source = "💬Hello, void!💬"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    string_token = next(t for t in tokens if t.type == TokenType.STRING)
    assert string_token.value == "Hello, void!"
    print("✓ test_strings passed")


def test_emoji_variables():
    """Test emoji variable names."""
    source = "🐱 🎯 🏆"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    emoji_vars = [t for t in tokens if t.type == TokenType.EMOJI_VAR]
    assert len(emoji_vars) == 3
    assert any(t.value == "🐱" for t in emoji_vars)
    assert any(t.value == "🎯" for t in emoji_vars)
    assert any(t.value == "🏆" for t in emoji_vars)
    print("✓ test_emoji_variables passed")


def test_temporal_whitespace():
    """Test temporal whitespace detection."""
    source = "a\nb    c d"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    # Should have newline, temporal tab (4 spaces), and micro-reversal (single space)
    assert any(t.type == TokenType.NEWLINE for t in tokens)
    assert any(t.type == TokenType.TEMPORAL_TAB for t in tokens)
    assert any(t.type == TokenType.MICRO_REVERSAL for t in tokens)
    
    # Check temporal offsets
    newline = next(t for t in tokens if t.type == TokenType.NEWLINE)
    assert newline.temporal_offset > 0  # Advances time
    
    tab = next(t for t in tokens if t.type == TokenType.TEMPORAL_TAB)
    assert tab.temporal_offset >= 10  # Big shift
    
    print("✓ test_temporal_whitespace passed")


def test_timeline_markers():
    """Test timeline begin and end markers."""
    source = "⏰BEGIN⏰ ⏳9999⏳ ⏰END⏰"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    assert any(t.type == TokenType.TIMELINE_BEGIN for t in tokens)
    assert any(t.type == TokenType.TIMELINE_END for t in tokens)
    assert any(t.type == TokenType.TEMPORAL_SIG for t in tokens)
    print("✓ test_timeline_markers passed")


def test_comments():
    """Test comment handling."""
    source = "🗨️ This is a comment\n42"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    # Comments should be skipped, so we should only have NEWLINE, NUMBER, and EOF
    token_types = [t.type for t in tokens]
    assert TokenType.COMMENT_SINGLE not in token_types
    assert TokenType.NUMBER in token_types
    print("✓ test_comments passed")


def test_malformed_string():
    """Test that malformed strings emit reality fracture tokens."""
    source = "💬unclosed string"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    assert any(t.type == TokenType.REALITY_FRACTURE for t in tokens)
    print("✓ test_malformed_string passed")


def test_backwards_reading():
    """Test backwards file reading with forward tokenization."""
    source = "line1\nline2\nline3"
    lexer = CECLexer(source, read_backwards=True)
    # After reading backwards, should have: line3\nline2\nline1
    
    tokens = list(lexer.tokenize())
    # Just verify it doesn't crash and produces tokens
    assert len(tokens) > 0
    assert tokens[-1].type == TokenType.EOF
    print("✓ test_backwards_reading passed")


def test_vibe_check():
    """Test vibe check calculation."""
    source = "💕 😊 🎉 💔 😢"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    vibe = calculate_vibe(tokens)
    
    assert "average_resonance" in vibe
    assert "peak_emotion" in vibe
    assert "valley_emotion" in vibe
    assert "trajectory" in vibe
    
    # Should have positive peak (🎉 = 1.0) and negative valley (😢 = -0.5)
    assert vibe["peak_emotion"] > 0.5
    assert vibe["valley_emotion"] < 0.0
    print("✓ test_vibe_check passed")


def test_complex_program():
    """Test tokenization of a more complex program."""
    source = """⏰BEGIN⏰ ⏳999⏳
🐱 ⟺ 42?
🐱 ⟸ 🐱 💕 13!
🕳️🖨️(🐱)!
⏰END⏰ 😊"""
    
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    # Verify we have the major token types
    token_types = [t.type for t in tokens]
    assert TokenType.TIMELINE_BEGIN in token_types
    assert TokenType.TIMELINE_END in token_types
    assert TokenType.EMOJI_VAR in token_types
    assert TokenType.DECLARE in token_types
    assert TokenType.ASSIGN in token_types
    assert TokenType.ADD_LOVE in token_types
    assert TokenType.VOID in token_types
    assert TokenType.HAPPY in token_types
    print("✓ test_complex_program passed")


def test_quantum_operators():
    """Test quantum-related operators."""
    source = "🔮 ⟨1|2|3⟩ 🎲"
    lexer = CECLexer(source)
    tokens = list(lexer.tokenize())
    
    token_types = [t.type for t in tokens]
    assert TokenType.QUANTUM_START in token_types
    assert TokenType.SUPERPOSITION_OPEN in token_types
    assert TokenType.SUPERPOSITION_CLOSE in token_types
    assert TokenType.SUPERPOSITION_SEP in token_types
    assert TokenType.COLLAPSE in token_types
    print("✓ test_quantum_operators passed")


def run_all_tests():
    """Run all tests."""
    print("\n🧪 Running CEC Lexer Tests...")
    print("="*50)
    
    tests = [
        test_basic_operators,
        test_emotional_resonance,
        test_emotional_contagion,
        test_numbers,
        test_strings,
        test_emoji_variables,
        test_temporal_whitespace,
        test_timeline_markers,
        test_comments,
        test_malformed_string,
        test_backwards_reading,
        test_vibe_check,
        test_complex_program,
        test_quantum_operators,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("="*50)
    print(f"\n📊 Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed!")
        return 0
    else:
        print("💔 Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
