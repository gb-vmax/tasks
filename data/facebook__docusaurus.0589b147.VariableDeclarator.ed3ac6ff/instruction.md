# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX code generation. When processing variable declarators, the output is malformed - the assignment operator and initialization expression appear before the variable identifier instead of after it.

### Reproduction

When compiling MDX content that includes variable declarations, the generated JavaScript output has the syntax reversed:

```js
// Expected output:
const myVar = 'value';

// Actual output:
const  = 'value'myVar;
```

This results in invalid JavaScript syntax that breaks the compilation process.

### Steps to reproduce:
1. Create an MDX file with a variable declaration
2. Process it through the MDX compiler
3. Observe the generated JavaScript output

The variable name and the assignment are in the wrong order, making the output syntactically invalid.

### Expected behavior

Variable declarations should be generated in the correct order: identifier first, then the assignment operator, then the initialization value.

```js
const myVar = 'value';
```

Not:
```js
const  = 'value'myVar;
```

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
