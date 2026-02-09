# Bug Report

### Describe the bug

Getting a `TypeError` when trying to use the compiler functionality. The error message says "Must provide [name] with compiler" even though I'm passing a valid compiler function.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkStringify);

// This throws an error
processor.stringify(ast);
```

The error occurs when calling `stringify` with a valid AST. It seems like the validation is incorrectly checking the compiler type.

### Expected behavior

The compiler should accept a function and process the AST without throwing a type error. The validation should allow functions to be passed as compilers.

### Additional context

This appears to be a regression - the same code was working in previous versions. The error message suggests it's expecting an object but compilers should be functions.

---
Repository: /testbed
