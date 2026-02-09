# Bug Report

### Describe the bug

When using JSX spread attributes with `jsx.mode` set to something other than `'preserve'`, the spread syntax is being left in the output instead of being properly transformed. The spread operators `{...}` are remaining in the compiled code when they should be removed for non-preserve modes.

### Reproduction

```js
// Input JSX with spread attribute
const element = <Component {...props} />;

// With jsx.mode: 'classic' or 'automatic'
// Expected: spread syntax removed/transformed
// Actual: spread syntax preserved in output
```

Configuration:
```js
{
  jsx: {
    mode: 'classic' // or 'automatic'
  }
}
```

### Expected behavior

When `jsx.mode` is set to `'classic'` or `'automatic'`, the JSX spread attribute syntax should be transformed/removed from the output. The spread operators should only be preserved when `jsx.mode` is explicitly set to `'preserve'`.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
