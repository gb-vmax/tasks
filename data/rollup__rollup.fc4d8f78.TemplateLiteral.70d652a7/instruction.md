# Bug Report

### Describe the bug

I'm encountering an issue with template literals that have no expressions (just a single quasi). It seems like the bundler is not correctly handling these simple template literals and is returning unexpected values.

### Reproduction

```js
// This template literal has no expressions, just a single quasi
const simple = `hello world`;

// When the bundler tries to get the literal value, 
// it returns UnknownValue instead of the actual string value
```

The problem occurs when you have a template literal without any interpolated expressions - basically just a string wrapped in backticks. The bundler should be able to determine the literal value in this case since there's nothing dynamic about it.

### Expected behavior

Template literals with a single quasi and no expressions should have their literal values properly extracted during the bundling process, just like regular string literals. The value should be `'hello world'` not `UnknownValue`.

### Additional context

This seems to affect tree-shaking and optimization of code that uses template literals without expressions. The bundler treats them as unknown values even though they're completely static.

---
Repository: /testbed
