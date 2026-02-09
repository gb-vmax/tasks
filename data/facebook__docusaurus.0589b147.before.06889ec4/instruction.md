# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where the parser fails to properly handle closing braces in expressions. It seems like the logic for detecting when an expression should be closed is inverted - the parser is throwing an "unexpected end of file" error when it shouldn't, and expressions that should be properly closed are being mishandled.

### Reproduction

```mdx
{someExpression}
```

When trying to parse basic MDX expressions with curly braces, the parser behaves incorrectly. The closing brace `}` is not being recognized properly, causing expressions to either fail parsing or continue when they should terminate.

### Expected behavior

MDX expressions enclosed in curly braces should parse correctly. When the parser encounters a closing brace `}` at the appropriate nesting level (size === 0), it should properly close the expression and return successfully. The parser should only throw an "unexpected end of file" error when it actually reaches the end of the file (code === null) with an unclosed expression.

### Additional context

This affects basic MDX expression syntax and makes it impossible to use simple expressions in MDX files. The issue appears to be related to the condition checking in the expression parser logic.

---
Repository: /testbed
