# Bug Report

### Describe the bug

I'm encountering an issue with parsing `const` declarations in the MDX parser. When trying to parse code that contains `const` variable declarations, the parser seems to be skipping the token consumption step, which causes the parser to get out of sync with the token stream.

### Reproduction

```js
const x = 1;
```

When the parser tries to process this declaration, it appears to conditionally skip calling `this.next()` for `const` declarations, which means the `const` keyword token is never consumed from the stream. This leads to incorrect parsing behavior where the parser is always one token behind where it should be.

### Expected behavior

The parser should properly consume all tokens in sequence, including the `const` keyword, and correctly parse constant variable declarations just like it does for `var` and `let` declarations.

### Additional context

This seems to affect the `parseVarStatement` function in the acorn parser vendored in the MDX package. The logic appears to have been modified to treat `const` differently from other variable declaration kinds, but this breaks the normal token consumption flow.

---
Repository: /testbed
