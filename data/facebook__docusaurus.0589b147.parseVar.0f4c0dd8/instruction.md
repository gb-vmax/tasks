# Bug Report

### Describe the bug

I'm experiencing an issue with parsing variable declarations in MDX files. When I have multiple const declarations separated by commas, only the first declaration is being parsed and the rest are being ignored.

### Reproduction

```js
const a = 1, b = 2, c = 3;
```

When parsing the above code, only `const a = 1` is being processed and `b` and `c` are not recognized as part of the same declaration statement.

### Expected behavior

All three variables should be parsed as part of a single const declaration statement with three declarators. The parser should continue reading comma-separated declarations until it encounters a different token.

### Additional context

This seems to affect const declarations specifically. The parser appears to be stopping after the first declarator instead of continuing to parse the remaining comma-separated variables.

---
Repository: /testbed
