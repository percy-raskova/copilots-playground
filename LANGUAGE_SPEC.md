# Chronolexical Emoji Calculus (CEC)

## Language Philosophy

CEC is a programming language where time flows backwards, emotions are operators, and emoji are your variables. The language exists in a quantum superposition of states until observed by the compiler.

## Core Principles

1. **Temporal Reversal**: Programs execute from bottom to top
2. **Emoji Variables**: All variables are represented by emoji characters
3. **Emotional Operators**: Operators have feelings that affect computation
4. **Quantum Superposition**: Values exist in multiple states simultaneously
5. **Dimensional Whitespace**: Different types of whitespace represent different temporal dimensions

---

## Formal Grammar

```ebnf
(* Chronolexical Emoji Calculus Grammar *)

program ::= timeline_end reality_collapse+ timeline_start

timeline_start ::= "⏰BEGIN⏰" temporal_signature
timeline_end ::= "⏰END⏰" emotional_state

temporal_signature ::= "⏳" NUMBER "⏳" (* milliseconds since heat death of universe *)

emotional_state ::= "😊" | "😢" | "😡" | "😱" | "🤔" | "🎉"

reality_collapse ::= statement TEMPORAL_WHITESPACE

statement ::= declaration 
            | assignment 
            | quantum_operation
            | emotional_conditional
            | temporal_loop
            | void_function
            | reality_check
            | comment

(* DECLARATIONS *)
declaration ::= emoji_var "⟺" value "?" (* ? means "maybe exists" *)

emoji_var ::= EMOJI_SYMBOL+

value ::= number_literal 
        | string_literal 
        | quantum_state
        | void_reference

number_literal ::= ["-"] DIGIT+ ["." DIGIT+] ["i"] (* i for imaginary *)

string_literal ::= "💬" ANY_CHAR* "💬"

quantum_state ::= "⟨" value ("|" value)+ "⟩" (* superposition of values *)

void_reference ::= "🕳️" (* the void *)

(* ASSIGNMENTS *)
assignment ::= emoji_var "⟸" expression "!" (* ! means "definitely happened" *)

expression ::= value
             | emoji_var
             | binary_operation
             | unary_operation
             | function_call

(* OPERATIONS *)
binary_operation ::= expression emotional_operator expression

emotional_operator ::= "💕" (* addition with love *)
                     | "💔" (* subtraction with heartbreak *)
                     | "🔥" (* multiplication with passion *)
                     | "💧" (* division with tears *)
                     | "⚡" (* exponentiation with excitement *)
                     | "🌙" (* modulo in darkness *)

unary_operation ::= emotional_prefix expression

emotional_prefix ::= "🎭" (* negate with drama *)
                   | "🌟" (* absolute value with glamour *)
                   | "👻" (* make imaginary *)
                   | "🌊" (* floor with waves *)
                   | "☁️" (* ceil to clouds *)

(* QUANTUM OPERATIONS *)
quantum_operation ::= "🔮" emoji_var "⟺" quantum_state "🔮"
                    | "🎲" emoji_var "⟸" emoji_var "🎲" (* collapse superposition *)

(* CONDITIONALS *)
emotional_conditional ::= "🤔" comparison "?"
                         indented_block
                         ["😮" (* else *)
                         indented_block]
                         "🤷"

comparison ::= expression comparator expression

comparator ::= "👍" (* greater than *)
             | "👎" (* less than *)
             | "🤝" (* equal *)
             | "💯" (* exactly equal *)
             | "🚫" (* not equal *)

indented_block ::= (TEMPORAL_TAB statement TEMPORAL_WHITESPACE)+

(* LOOPS *)
temporal_loop ::= backwards_loop | quantum_loop

backwards_loop ::= "🔄" emoji_var "⟸" expression "⤵️" expression
                  indented_block
                  "🛑"

quantum_loop ::= "🌀" emoji_var "∈" quantum_state
                indented_block
                "🌪️"

(* FUNCTIONS *)
void_function ::= "🕳️" function_name "(" parameter_list ")" "{"
                 statement+
                 "🎁" return_value (* gift from the void *)
                 "}"

function_name ::= EMOJI_SYMBOL+

parameter_list ::= emoji_var ("," emoji_var)*

return_value ::= expression | "🕳️"

function_call ::= function_name "(" argument_list ")"

argument_list ::= expression ("," expression)*

(* REALITY CHECKS *)
reality_check ::= "🚨" expression "🚨" (* assert reality matches expectation *)

(* COMMENTS *)
comment ::= "💭" ANY_CHAR* "💭"
          | "🗨️" ANY_CHAR* TEMPORAL_WHITESPACE (* single line *)

(* WHITESPACE DIMENSIONS *)
TEMPORAL_WHITESPACE ::= "\n" (* moves forward in time *)
TEMPORAL_TAB ::= "    " (* indents into parallel dimension *)
REVERSE_SPACE ::= " " (* backwards micro-adjustment *)

(* LEXICAL TOKENS *)
EMOJI_SYMBOL ::= (* any valid emoji character *)
DIGIT ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
NUMBER ::= DIGIT+
ANY_CHAR ::= (* any Unicode character except closing delimiter *)
```

---

## Special Features

### 1. Temporal Reversal
Programs execute from the `⏰END⏰` marker upward to the `⏰BEGIN⏰` marker. This means the last statement executes first.

### 2. Quantum Superposition
Variables can exist in multiple states simultaneously:
```
🐱 ⟺ ⟨5|7|13⟩?
```
The variable `🐱` is simultaneously 5, 7, and 13 until observed.

### 3. Emotional Operators
Operators have feelings that subtly affect their behavior:
- `💕` (addition with love) - slightly biases results toward positive numbers
- `💔` (subtraction with heartbreak) - might unexpectedly round down
- `🔥` (multiplication with passion) - can overflow with enthusiasm

### 4. The Void
`🕳️` represents the absence of value, similar to null/void but with existential implications.

### 5. Reality Checks
`🚨` markers assert that reality matches your expectations. If not, the universe collapses (program crashes).

---

## Reserved Emoji

The following emoji have special meaning in CEC:

**Control Flow:**
- ⏰ - Timeline markers
- ⏳ - Temporal signature
- 🔄 - Loop start
- 🛑 - Loop end
- 🌀 - Quantum loop start
- 🌪️ - Quantum loop end
- 🤔 - If statement
- 😮 - Else clause
- 🤷 - End if

**Operators:**
- ⟺ - Declaration
- ⟸ - Assignment
- 💕💔🔥💧⚡🌙 - Arithmetic operators
- 🎭🌟👻🌊☁️ - Unary operators
- 👍👎🤝💯🚫 - Comparison operators

**Quantum:**
- 🔮 - Quantum operation
- 🎲 - Collapse superposition
- ⟨ ⟩ - Superposition delimiters

**Functions:**
- 🕳️ - Void/function marker
- 🎁 - Return statement

**Literals:**
- 💬 - String delimiter
- 🚨 - Reality check
- 💭 - Multi-line comment
- 🗨️ - Single-line comment

**Special:**
- ? - Maybe exists
- ! - Definitely happened
- ⤵️ - Down to (in loops)
- ∈ - Element of

---

## Type System

CEC has a quantum type system where types are probabilistic:

1. **Numbers**: Can be real, imaginary, or complex
   - Real: `42`
   - Imaginary: `42i`
   - Complex: `3+4i`

2. **Strings**: Enclosed in 💬
   - `💬Hello, void!💬`

3. **Quantum States**: Superposition of values
   - `⟨1|2|3⟩`

4. **Void**: The absence
   - `🕳️`

5. **Emoji**: Variable identifiers
   - Any emoji or combination of emoji

---

## Execution Model

1. **Parse**: Source is read from top to bottom
2. **Reverse**: Execution order is reversed
3. **Execute**: Statements run from bottom to top
4. **Collapse**: Quantum states collapse when observed
5. **Reflect**: Final state is reflected through emotional lens

The emotional state at `⏰END⏰` affects how the program result is interpreted:
- 😊 - Success, all is well
- 😢 - Success, but at what cost?
- 😡 - Error state, program is angry
- 😱 - Panic, undefined behavior
- 🤔 - Uncertain, Heisenberg would approve
- 🎉 - Celebration, program exceeded expectations

---

## Memory Model

CEC uses an **Emotional Heap** where:
- Memory addresses are feelings
- Garbage collection happens when emotions fade
- Stack grows downward (because time reverses)
- Cache is pre-heated (it already knows what you'll compute)

---

## Standard Library Functions

CEC provides several built-in void functions:

```
🕳️🖨️(value)     - Print to temporal console
🕳️📥(prompt)    - Input from future user
🕳️🎵(frequency) - Emit sound at frequency
🕳️🌈(value)     - Colorize output
🕳️💤(duration)  - Sleep (wait in past)
🕳️🔔(message)   - Alert (ring bell in past)
```

---

## Error Handling

Errors in CEC are called **Reality Fractures**:

- `💥 Temporal Paradox` - Contradictory timeline
- `🌋 Emotional Overflow` - Too many feelings
- `🖤 Void Collapse` - Null reference
- `🎪 Quantum Entanglement` - Circular dependency
- `🌩️ Reality Mismatch` - Failed assertion

---

## Compilation Directives

```
#⚙️ optimize:passion
#🔊 verbosity:eleven
#🌡️ temperature:absolute_zero
#🎨 theme:cyberpunk
```

These directives exist in the metadata dimension and affect compilation behavior.

---

## Philosophy

CEC embraces the absurd while maintaining computational completeness. It's a reminder that programming languages are human constructs, and we can question every assumption. Why should time flow forward? Why can't operators have emotions? Why not use emoji as identifiers?

The language is Turing complete (probably), quantum uncertain (definitely), and temporally reversed (always).

Welcome to Chronolexical Emoji Calculus. The future is behind us.
