# Bug Report

### Describe the bug

When using a `switch` statement with only a single `case` block, the output is not being rendered correctly. The case statement and its body seem to be missing from the generated code.

### Reproduction

```js
switch (value) {
  case 'foo':
    console.log('bar');
    break;
}
```

After bundling, the switch statement appears incomplete or malformed in the output. The single case block is not being included in the final code.

### Expected behavior

Switch statements with a single case should render properly in the bundled output, including the case label and its body.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
