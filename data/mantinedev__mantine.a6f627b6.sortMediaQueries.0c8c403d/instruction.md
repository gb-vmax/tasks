# Bug Report

### Describe the bug

I'm experiencing an issue with responsive styles when using media queries with the Box component. The styles are being applied in the wrong order, causing larger breakpoints to be overridden by smaller ones.

### Reproduction

```jsx
<Box
  w={{ base: 100, sm: 200, md: 300, lg: 400 }}
>
  Content
</Box>
```

When resizing the browser window, the width values don't apply correctly at different breakpoints. For example, at `lg` breakpoint, the width might still be using the `sm` value instead of the `lg` value.

### Expected behavior

Media queries should be sorted in ascending order so that larger breakpoints override smaller ones. The `lg` breakpoint styles should take precedence over `md`, which should take precedence over `sm`, etc.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
