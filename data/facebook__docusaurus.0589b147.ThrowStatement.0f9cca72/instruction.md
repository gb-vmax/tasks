# Bug Report

### Describe the bug

I'm encountering an issue with MDX code generation where `throw` statements are being generated with incorrect syntax. The `throw` keyword appears after the expression instead of before it, resulting in invalid JavaScript code.

### Reproduction

When processing MDX content that contains throw statements, the generated output has the throw keyword in the wrong position:

```js
// Expected output:
throw new Error('message');

// Actual output:
new Error('message')throw ;
```

This makes the generated code unparseable and breaks compilation.

### Steps to reproduce
1. Create an MDX file with a throw statement in a JavaScript expression
2. Process the file through the MDX compiler
3. Observe the generated JavaScript output

### Expected behavior

The `throw` keyword should be written before the argument expression, not after it. The generated code should be valid JavaScript that can be executed without syntax errors.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
