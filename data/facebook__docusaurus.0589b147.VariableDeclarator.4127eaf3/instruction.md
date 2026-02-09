# Bug Report

### Describe the bug

Variable declarations are being generated incorrectly in the MDX output. When a variable is declared without an initializer, the code generator is still outputting an assignment operator and trying to access a null `init` property, which causes issues.

### Reproduction

```js
// Input MDX with variable declaration
export let myVar;

// Expected output:
// export let myVar;

// Actual output (causes error):
// export let myVar = undefined;
// or fails to generate properly
```

The issue occurs when processing variable declarators that don't have an initial value. The generator seems to be handling the assignment logic backwards.

### Expected behavior

Variable declarations without initializers should be output as-is, without any assignment operator or attempting to access the `init` property when it's null.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
