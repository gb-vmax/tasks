# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in generated JavaScript output. It appears that semicolons are being duplicated at the end of variable declaration statements, which is causing invalid syntax in the generated code.

### Reproduction

When processing MDX content that includes variable declarations, the output contains double semicolons:

```js
// Input MDX with variable declaration
const myVar = 'value'

// Generated output has duplicate semicolons
const myVar = 'value';;
```

This happens consistently with all types of variable declarations (`const`, `let`, `var`).

### Expected behavior

Variable declarations should end with a single semicolon in the generated JavaScript output:

```js
const myVar = 'value';
```

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

The duplicate semicolons are causing syntax issues in the generated code. This seems to have appeared recently, possibly after some code formatting changes.

---
Repository: /testbed
