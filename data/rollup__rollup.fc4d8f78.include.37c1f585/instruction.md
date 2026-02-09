# Bug Report

### Describe the bug

I'm encountering an issue where variable declarations are being included multiple times in the bundled output. It seems like the logic for checking whether a node has already been included isn't working correctly.

### Reproduction

```js
// input.js
const foo = 'test';
console.log(foo);
console.log(foo);
```

When bundling this code, the variable declaration for `foo` appears to be processed repeatedly, leading to unexpected behavior in the output bundle.

### Expected behavior

Each variable declarator should only be included once in the bundle, even if the variable is referenced multiple times. The check for whether a node has already been included should prevent duplicate processing.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
