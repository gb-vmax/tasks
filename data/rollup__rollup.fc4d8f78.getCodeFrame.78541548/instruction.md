# Bug Report

### Describe the bug

The code frame highlighting in error messages is pointing to the wrong line. When an error occurs, the caret (^) that should indicate the exact error position appears on the line below where the actual error is.

### Reproduction

When triggering an error at a specific line in the source code, the generated code frame shows the error indicator shifted by one line:

```js
// If error occurs on line 5
3: const foo = 'bar';
4: const baz = 'qux';
5: const broken = syntax error here;  // actual error line
   ^  // but the caret appears on line 6 instead
6: const next = 'line';
```

The error marker is consistently off by one line, making it harder to identify the actual location of syntax errors or other issues.

### Expected behavior

The caret should appear directly under the column position on the same line where the error actually occurred, not on the following line.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
