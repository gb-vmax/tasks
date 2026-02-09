# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow tag parsing. When a JSX tag is followed by whitespace, the parser seems to handle it incorrectly, and when the code encounters certain characters (like `<` or `{`), the logic appears inverted from what it should be.

### Reproduction

```mdx
<Component />
  
Some text here
```

Or with expressions:

```mdx
<MyTag />
{someExpression}
```

The parser doesn't seem to correctly handle the whitespace after the closing tag, and the conditions for checking whether to continue parsing or handle specific characters appear to be backwards.

### Expected behavior

The parser should correctly handle whitespace following JSX flow tags and properly distinguish between different code paths based on the character being processed. Tags followed by whitespace or expressions should be parsed correctly without unexpected behavior.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
