# Bug Report

### Describe the bug

I'm experiencing an issue with keyword parsing where the token type and value seem to be getting mixed up. When parsing code that contains JavaScript keywords (like `if`, `while`, `function`, etc.), the parser appears to be returning incorrect token information.

### Reproduction

```js
// Parse code containing a keyword
const code = 'if (true) { }';
const ast = parse(code);

// The token for 'if' has incorrect type/value
// Expected: token type should be keyword type, value should be 'if'
// Actual: token type and value are swapped
```

### Expected behavior

When parsing keywords, the parser should correctly assign:
- The token type as the appropriate keyword type
- The token value as the actual keyword string (e.g., 'if', 'while', 'function')

Currently it seems like these two values are being passed in the wrong order, causing keywords to be misidentified or have incorrect metadata.

### Additional context

This affects all JavaScript keywords during parsing. The issue appears to be in the word reading logic where tokens are being finalized with their arguments in an unexpected order.

---
Repository: /testbed
