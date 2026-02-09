# Bug Report

### Describe the bug

JSX spread attributes are being incorrectly removed when using `jsx: 'preserve'` mode. The spread syntax `{...props}` gets stripped from the output even though the preserve mode should keep JSX syntax intact.

### Reproduction

```jsx
// Input code
const Component = () => <div {...props} />;

// With jsx: 'preserve' option
// Expected: <div {...props} />
// Actual: <div />
```

The spread attributes are being removed when they should be preserved. This breaks the JSX output when the preserve mode is explicitly set.

### Expected behavior

When using `jsx: 'preserve'`, all JSX syntax including spread attributes should remain unchanged in the output. The `{...props}` syntax should not be stripped.

### System Info
- Rollup version: latest
- JSX mode: preserve

---
Repository: /testbed
