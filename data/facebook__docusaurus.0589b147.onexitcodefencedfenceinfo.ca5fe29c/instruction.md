# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in markdown where the language identifier is not being correctly assigned to fenced code blocks. The `lang` property appears to be set incorrectly or contains unexpected data.

### Reproduction

```markdown
```javascript
console.log('hello');
```
```

When parsing this markdown, the code block's language information is not properly captured. The `lang` property on the resulting AST node doesn't match what was specified in the fence info string.

### Expected behavior

The parser should correctly extract and assign the language identifier (e.g., "javascript") to the code block's `lang` property. The AST node for the fenced code block should have `lang: 'javascript'`.

### Additional context

This seems to affect all fenced code blocks with language identifiers. The issue appears to be related to how the fence info string is being processed during parsing.

---
Repository: /testbed
