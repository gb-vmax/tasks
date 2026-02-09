# Bug Report

### Describe the bug

When bundling code with a switch statement that has a last case without a break, the last case is not being included in the output bundle even when it should be. This appears to affect tree-shaking behavior for switch statements.

### Reproduction

```js
function test(value) {
  switch(value) {
    case 'a':
      console.log('case a');
      break;
    case 'b':
      console.log('case b');
      break;
    case 'c':
      console.log('case c');
      // no break - falls through or ends
  }
}

test('c');
```

### Expected behavior

The last case in the switch statement should be included in the bundle when it's reachable. Currently it seems like the last case is being skipped during tree-shaking analysis, resulting in incomplete output.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
