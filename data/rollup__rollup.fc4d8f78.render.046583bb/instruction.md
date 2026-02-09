# Bug Report

### Describe the bug

JSX spread attributes are being incorrectly stripped out when using `jsx: 'preserve'` mode. The spread syntax (`{...props}`) is removed from the output even though preserve mode should keep the JSX syntax intact.

### Reproduction

```jsx
// Input code with jsx: 'preserve'
const Component = <div {...props} />;
```

When bundling with `jsx: 'preserve'` option, the spread attribute syntax gets removed from the output instead of being preserved.

### Expected behavior

With `jsx: 'preserve'` mode enabled, the JSX spread attributes should remain unchanged in the output:

```jsx
// Expected output
const Component = <div {...props} />;
```

Instead, the spread syntax is being stripped out, which breaks the JSX structure.

### System Info
- Rollup version: latest
- JSX mode: preserve

---
Repository: /testbed
