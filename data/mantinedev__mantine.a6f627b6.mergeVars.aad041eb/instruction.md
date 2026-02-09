# Bug Report

### Describe the bug

When merging CSS variables with `mergeVars`, the order of precedence is incorrect. Variables defined earlier in the array are overriding variables defined later, when it should be the opposite - later variables should take precedence over earlier ones.

### Reproduction

```js
const vars1 = {
  root: {
    '--color-primary': 'blue',
    '--spacing': '10px'
  }
};

const vars2 = {
  root: {
    '--color-primary': 'red'
  }
};

const merged = mergeVars([vars1, vars2]);

// Expected: '--color-primary' should be 'red' (from vars2)
// Actual: '--color-primary' is 'blue' (from vars1)
```

### Expected behavior

When merging multiple variable objects, variables from later objects in the array should override variables from earlier objects. This is the standard behavior for merging operations where the last value wins.

In the example above, since `vars2` comes after `vars1` in the array, its `--color-primary: 'red'` should be the final value in the merged result.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
