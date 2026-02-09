# Bug Report

### Describe the bug

When merging CSS variables with `mergeVars`, the order of precedence seems to be reversed. Variables that should be overridden are taking priority over the ones that should override them.

### Reproduction

```js
const baseVars = {
  root: {
    '--color': 'blue',
    '--size': '10px'
  }
};

const overrideVars = {
  root: {
    '--color': 'red'
  }
};

const merged = mergeVars([baseVars, overrideVars]);

// Expected: '--color' should be 'red' (from overrideVars)
// Actual: '--color' is 'blue' (from baseVars)
console.log(merged.root['--color']); // outputs 'blue' instead of 'red'
```

### Expected behavior

Later variables in the array should override earlier ones. In the example above, `overrideVars` comes after `baseVars`, so its `--color: 'red'` should take precedence over the `--color: 'blue'` from `baseVars`.

The merged result should have `--color: 'red'`, but it's keeping the value from the first object instead.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
