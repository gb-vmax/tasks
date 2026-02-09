# Bug Report

### Describe the bug

JSX text content is not being rendered correctly when using different JSX modes. The text appears to be processed incorrectly, causing either missing content or unexpected transformations in the output.

### Reproduction

```jsx
// With jsx.mode set to 'preserve'
const element = <div>Hello World</div>

// Expected: Text content should remain as-is
// Actual: Text content gets stringified/transformed when it shouldn't
```

When I set the JSX mode to 'preserve', the text nodes are being transformed instead of preserved. Conversely, in other modes where text should be transformed, it's being left as-is.

### Expected behavior

- When `jsx.mode` is set to `'preserve'`, JSX text content should be left untouched
- When `jsx.mode` is set to other values (like `'classic'` or `'automatic'`), JSX text should be properly transformed (whitespace trimming/merging, JSON stringification)

### Additional context

This seems to affect all JSX text nodes, including those with whitespace that should normally be normalized. The behavior is completely inverted from what the mode setting indicates.

---
Repository: /testbed
