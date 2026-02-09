# Bug Report

### Describe the bug

When passing CSS properties with `undefined` values to inline styles, they are being rendered in the output string instead of being filtered out. This causes invalid CSS to be generated.

### Reproduction

```js
const styles = {
  color: 'red',
  backgroundColor: undefined,
  fontSize: '16px'
}

// The generated CSS string incorrectly includes the undefined value
// Expected: "color:red;font-size:16px;"
// Actual: "color:red;background-color:undefined;font-size:16px;"
```

### Expected behavior

CSS properties with `undefined` values should be excluded from the generated CSS string, similar to how React handles undefined inline styles. Only properties with actual values should appear in the output.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
