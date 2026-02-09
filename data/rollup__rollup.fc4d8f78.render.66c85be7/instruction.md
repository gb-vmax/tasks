# Bug Report

### Describe the bug

I'm encountering an issue with `throw` statement rendering where the output is generating invalid JavaScript syntax. When a `throw` statement is used in the code, the generated output appears to be missing necessary whitespace between the `throw` keyword and its argument, resulting in syntax errors.

### Reproduction

```js
// Input code
function test() {
  throw new Error('test');
}
```

After bundling, the throw statement doesn't render correctly and produces malformed JavaScript that fails to parse.

### Expected behavior

The `throw` statement should render with proper spacing between the keyword and its argument, producing valid JavaScript like:
```js
throw new Error('test');
```

Instead, the spacing seems to be handled incorrectly, potentially causing the keyword and argument to run together or be improperly formatted.

### Additional context

This appears to affect throw statements in general, particularly when the argument immediately follows the `throw` keyword. The generated code should maintain valid JavaScript syntax with appropriate whitespace.

---
Repository: /testbed
