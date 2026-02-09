# Bug Report

### Describe the bug

I'm experiencing an issue with JSX parsing in MDX where whitespace handling appears to be broken. When using JSX expressions with whitespace (spaces or unicode whitespace characters), the parser doesn't properly handle the tokens, causing unexpected behavior.

### Reproduction

```mdx
<Component
  prop={
    value
  }
/>
```

Or with unicode whitespace:

```mdx
<Component prop={value  } />
```

The whitespace inside JSX expressions seems to cause parsing issues. The tokenizer appears to be exiting the whitespace state prematurely or not consuming whitespace tokens correctly.

### Expected behavior

Whitespace inside JSX expressions should be properly consumed and the parser should correctly handle both regular spaces and unicode whitespace characters without breaking the token flow. The `esWhitespace` state should be properly entered and exited.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
