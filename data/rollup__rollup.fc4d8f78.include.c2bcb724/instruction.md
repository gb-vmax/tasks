# Bug Report

### Describe the bug

I'm experiencing an issue with labeled break statements in switch cases. When a break statement has a label, it seems to be incorrectly flagged as breaking out of the switch statement itself, causing unexpected tree-shaking behavior.

### Reproduction

```js
outer: switch (condition) {
  case 'a':
    inner: while (true) {
      break outer;
    }
    console.log('This should be removed'); // Should be tree-shaken
    break;
  case 'b':
    console.log('case b');
    break;
}
```

In this example, the code after `break outer;` should be recognized as unreachable and removed during tree-shaking, but it appears that labeled breaks are not being handled correctly. The control flow analysis seems to treat labeled breaks the same as unlabeled ones.

### Expected behavior

When a break statement has a label, it should only mark the labeled loop/block as having a break, not the immediate enclosing switch statement. The tree-shaking should correctly identify unreachable code after labeled break statements.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
