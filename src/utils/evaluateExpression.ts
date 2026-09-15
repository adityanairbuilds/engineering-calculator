/**
 * Tiny recursive-descent evaluator for the basic calculator.
 * Grammar (highest precedence last):
 *   expr   := term (('+' | '-') term)*
 *   term   := unary (('*' | '/') unary)*
 *   unary  := '-' unary | '√' unary | power
 *   power  := postfix ('^' unary)?              (right-assoc)
 *   postfix:= primary '%'*                       (each % divides by 100)
 *   primary:= number | '(' expr ')'
 */

type Token = { type: 'num'; value: number } | { type: 'op'; value: string };

/** Display characters the keypad emits, mapped to the operators the parser uses. */
const OP_ALIASES: Record<string, string> = { '×': '*', '÷': '/' };

function tokenize(input: string): Token[] {
  const tokens: Token[] = [];
  let i = 0;
  while (i < input.length) {
    const ch = input[i];
    if (/\s/.test(ch)) {
      i++;
    } else if (/[0-9.]/.test(ch)) {
      let j = i + 1;
      while (j < input.length && /[0-9.]/.test(input[j])) j++;
      const text = input.slice(i, j);
      if ((text.match(/\./g) || []).length > 1) throw new Error('Invalid number');
      tokens.push({ type: 'num', value: Number(text) });
      i = j;
    } else if ('+-*/^%()√×÷'.includes(ch)) {
      tokens.push({ type: 'op', value: OP_ALIASES[ch] ?? ch });
      i++;
    } else {
      throw new Error(`Unexpected character "${ch}"`);
    }
  }
  return tokens;
}

class Parser {
  private pos = 0;
  private tokens: Token[];
  constructor(tokens: Token[]) {
    this.tokens = tokens;
  }

  private peek(): Token | undefined {
    return this.tokens[this.pos];
  }

  /** True when the next token is one of the given operators. */
  private atOp(...operators: string[]): boolean {
    const t = this.peek();
    return t?.type === 'op' && operators.includes(t.value);
  }

  private consume(value?: string): Token {
    const t = this.tokens[this.pos];
    if (!t || (value && !(t.type === 'op' && t.value === value))) {
      throw new Error(value ? `Expected "${value}"` : 'Unexpected end of expression');
    }
    this.pos++;
    return t;
  }

  parse(): number {
    const value = this.expr();
    if (this.pos !== this.tokens.length) throw new Error('Unexpected input');
    return value;
  }

  private expr(): number {
    let value = this.term();
    while (this.atOp('+', '-')) {
      const op = this.consume().value;
      const rhs = this.term();
      value = op === '+' ? value + rhs : value - rhs;
    }
    return value;
  }

  private term(): number {
    let value = this.unary();
    while (this.atOp('*', '/')) {
      const op = this.consume().value;
      const rhs = this.unary();
      if (op === '/' && rhs === 0) throw new Error('Cannot divide by zero');
      value = op === '*' ? value * rhs : value / rhs;
    }
    return value;
  }

  private unary(): number {
    if (this.atOp('-')) {
      this.consume('-');
      return -this.unary();
    }
    if (this.atOp('√')) {
      this.consume('√');
      const value = this.unary();
      if (value < 0) throw new Error('Cannot take the square root of a negative number');
      return Math.sqrt(value);
    }
    return this.power();
  }

  private power(): number {
    const base = this.postfix();
    if (this.atOp('^')) {
      this.consume('^');
      const exponent = this.unary();
      return base ** exponent;
    }
    return base;
  }

  private postfix(): number {
    let value = this.primary();
    while (this.atOp('%')) {
      this.consume('%');
      value = value / 100;
    }
    return value;
  }

  private primary(): number {
    const t = this.peek();
    if (!t) throw new Error('Unexpected end of expression');
    if (t.type === 'num') {
      this.consume();
      return t.value;
    }
    if (t.type === 'op' && t.value === '(') {
      this.consume('(');
      const value = this.expr();
      this.consume(')');
      return value;
    }
    throw new Error('Unexpected token');
  }
}

export function evaluateExpression(input: string): number {
  const tokens = tokenize(input);
  if (tokens.length === 0) throw new Error('Empty expression');
  const result = new Parser(tokens).parse();
  if (!Number.isFinite(result)) throw new Error('Result is undefined');
  return result;
}
