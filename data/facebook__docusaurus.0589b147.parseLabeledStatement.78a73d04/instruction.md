# Bug Report

### Describe the bug

I'm encountering a critical issue where labeled statements in JavaScript code are not being parsed correctly. When I try to use labeled statements (like `labelName: statement`), the parser fails completely or produces unexpected results.

### Reproduction

```js
// This should work but doesn't
myLabel: for (let i = 0; i < 10; i++) {
  if (i === 5) break myLabel;
}

// Also fails with nested labels
outer: for (let i = 0; i < 3; i++) {
  inner: for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) break outer;
  }
}
```

### Expected behavior

Labeled statements should be parsed correctly and allow breaking/continuing to specific labels. The parser should:
1. Recognize label syntax (`labelName: statement`)
2. Handle nested labels properly
3. Detect duplicate label names and raise appropriate errors

### Additional context

This appears to affect any code that uses labeled statements, including:
- Labeled loops (for, while, do-while)
- Labeled blocks
- Break/continue statements with label references

The parsing seems to be completely broken for this JavaScript feature. Not sure what changed but this is blocking our ability to process valid JavaScript code.

---
Repository: /testbed
