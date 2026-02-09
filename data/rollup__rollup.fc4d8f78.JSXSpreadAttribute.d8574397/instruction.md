# Bug Report

### Describe the bug

When using JSX spread attributes with `jsx: 'preserve'` mode, the spread syntax is being incorrectly stripped from the output. The curly braces and spread operator are removed even though the JSX should be preserved as-is.

### Reproduction

```jsx
// Input JSX
<Component {...props} />

// With jsx: 'preserve' in rollup config
export default {
  jsx: {
    mode: 'preserve'
  }
}
```

### Expected behavior

When `jsx: 'preserve'` is set, the JSX spread attribute should remain unchanged in the output:
```jsx
<Component {...props} />
```

### Actual behavior

The spread syntax gets stripped and the output is malformed or the braces/spread operator are removed when they shouldn't be.

### System Info
- Rollup version: latest
- JSX mode: preserve

---
Repository: /testbed
