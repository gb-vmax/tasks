# Bug Report

### Describe the bug

When bundling ES modules with exports that have expressions, the generated export code is using the wrong variable name. The exported constant declaration is being assigned the value of `specifier.exported` instead of `specifier.expression`, which causes the wrong value to be exported.

### Reproduction

```js
// input module
export const myVar = someExpression();

// expected output
const myVar = someExpression();
export { myVar };

// actual output (broken)
const myVar = myVar; // references itself instead of the expression
export { myVar };
```

This happens when:
1. You have a named export with an expression
2. The bundler generates the ES output format
3. The exported name differs from or references the local binding

### Expected behavior

The generated code should assign the expression result to the local variable, not assign the exported name to itself. The constant should be initialized with the actual expression value.

### System Info
- Rollup version: latest
- Output format: ES modules

---
Repository: /testbed
