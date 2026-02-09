# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in the generated output. When bundling code with multiple variable declarations, the output seems to be malformed - semicolons are being added in incorrect places, and the declarations aren't being rendered properly.

### Reproduction

```js
// Input code with variable declarations
const foo = 1, bar = 2;
let x = 3, y = 4;

// After bundling, the output is incorrect
// Variables that should be kept together are being split incorrectly
```

The issue appears when:
1. You have variable declarations with multiple declarators (comma-separated)
2. Some declarations are exported and others aren't
3. The bundler tries to optimize which declarations to include

### Expected behavior

Variable declarations should be rendered correctly in the output, maintaining proper JavaScript syntax. Semicolons should only be added where appropriate, and the logic for determining when declarations should be grouped or separated should work consistently.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
