# Bug Report

### Describe the bug

I'm experiencing an issue with automatic semicolon insertion (ASI) in the MDX parser. It seems like the parser is not correctly detecting when semicolons can be inserted, particularly at end-of-file positions and when checking for line breaks.

### Reproduction

```js
// This code should parse correctly with ASI
const example = `
function test() {
  return {
    value: 1
  }
}
`

// Parser fails to recognize valid ASI positions
// Expected: successful parse
// Actual: parsing errors or incorrect behavior
```

When parsing MDX content that relies on automatic semicolon insertion, the parser doesn't properly detect EOF or line break conditions. This causes valid JavaScript/MDX code to either fail parsing or be parsed incorrectly.

### Expected behavior

The parser should correctly identify positions where semicolons can be automatically inserted according to JavaScript ASI rules, including:
- At end of file (EOF)
- Before closing braces
- After line breaks

### System Info
- MDX version: 3.0.0
- Node version: Latest

This appears to be affecting the `canInsertSemicolon` function in the parser logic.

---
Repository: /testbed
