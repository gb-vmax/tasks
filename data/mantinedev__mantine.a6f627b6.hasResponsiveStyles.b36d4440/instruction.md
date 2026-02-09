# Bug Report

### Describe the bug

When using responsive style props with only the `base` breakpoint, the styles are being incorrectly treated as responsive. This causes unnecessary style generation and potentially affects performance.

### Reproduction

```jsx
<Box
  p={{ base: 'md' }}
>
  Content
</Box>
```

In the above example, since only the `base` breakpoint is specified, this should be treated as a non-responsive style prop. However, it's currently being processed as if it has responsive styles.

### Expected behavior

When a style prop object contains only the `base` breakpoint (e.g., `{ base: 'md' }`), it should be treated the same as a simple value (e.g., `'md'`) and not trigger responsive style handling.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
