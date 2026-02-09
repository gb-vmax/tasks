# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations where semicolons are being added in incorrect positions, resulting in malformed output code. It seems like the semicolon insertion logic is checking for the wrong condition.

### Reproduction

When bundling code with variable declarations, the output includes duplicate or misplaced semicolons. 

Example input:
```js
const foo = 1;
const bar = 2;
```

The semicolons are being added even when they already exist, or being placed before the declarations are fully rendered, which breaks the output.

### Expected behavior

Variable declarations should be rendered with proper semicolon placement - semicolons should only be added when they're missing from the original code, and they should be added after all declarations are rendered, not before.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
