# Bug Report

### Describe the bug

I'm experiencing an issue with switch case rendering where the colon (`:`) after case labels gets duplicated or appears in the wrong position in the generated output. This seems to affect both regular `case` statements and `default` cases.

### Reproduction

```js
switch (value) {
  case 'test':
    console.log('hello');
    break;
  default:
    console.log('default');
}
```

When this code is processed, the output has malformed syntax around the colon character. The colon either appears twice or is positioned incorrectly relative to the case label.

### Expected behavior

The switch statement should be rendered correctly with proper colon placement:
- `case 'test':` should have exactly one colon after the test expression
- `default:` should have exactly one colon after the keyword
- No extra characters or spacing issues around the colon

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
