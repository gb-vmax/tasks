# Bug Report

### Describe the bug

I'm encountering an issue with the MDX code generator where `return` statements are being generated with incorrect syntax. The return value appears after the semicolon instead of before it.

### Reproduction

When compiling MDX that generates return statements with arguments, the output JavaScript has malformed syntax:

```js
// Generated output looks like:
return; someValue

// Instead of the expected:
return someValue;
```

This results in JavaScript syntax errors when the generated code is executed. The return statement is terminated early with the semicolon, and then the actual return value appears as a separate (unreachable) statement.

### Expected behavior

Return statements should be generated with proper JavaScript syntax where the argument comes before the semicolon:
```js
return someValue;
```

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is breaking my MDX compilation pipeline. Any help would be appreciated!

---
Repository: /testbed
