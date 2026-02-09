# Bug Report

### Describe the bug

I'm encountering an issue with `for...in` statement rendering where there's incorrect spacing between the `in` keyword and the right-hand side expression. The generated code has malformed syntax with missing spaces.

### Reproduction

```js
// Input code
for (const key in object) {
  console.log(key);
}

// After bundling, the output becomes:
for (const key inobject) {
  console.log(key);
}
```

The space after `in` is missing, which causes a syntax error when the bundled code is executed.

### Expected behavior

The bundler should preserve proper spacing around the `in` keyword in `for...in` loops. The output should maintain valid JavaScript syntax:

```js
for (const key in object) {
  console.log(key);
}
```

### Additional context

This seems to happen specifically with `for...in` statements. Regular `for` loops and `for...of` loops appear to work correctly. The issue breaks the generated bundle completely since it produces invalid JavaScript syntax.

---
Repository: /testbed
