# Bug Report

### Describe the bug

I'm experiencing an issue with semicolon insertion in expression statements. After a recent change, semicolons are being inserted at incorrect positions, causing syntax errors in the generated code.

### Reproduction

When processing expression statements that don't already have a semicolon, the bundler is adding semicolons at the wrong position - one character too early.

Example input:
```js
console.log('hello')
someFunction()
```

The semicolon gets inserted before the last character of the statement instead of at the actual end, resulting in malformed output like:
```js
console.log('hello';)
someFunction(;)
```

### Expected behavior

Semicolons should be appended at the end of expression statements (after all characters), not before the last character. The output should be:
```js
console.log('hello');
someFunction();
```

### Additional context

This seems to affect all expression statements that are missing trailing semicolons. The issue appears to be related to how the end position of the statement is being calculated when checking for and inserting semicolons.

---
Repository: /testbed
