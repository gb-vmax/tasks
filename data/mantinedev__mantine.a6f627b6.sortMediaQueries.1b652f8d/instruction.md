# Bug Report

### Describe the bug

Media queries are being applied in the wrong order when using responsive style props. Styles for larger breakpoints are being overridden by smaller breakpoints instead of the other way around.

### Reproduction

```tsx
<Box
  p={{ base: 10, sm: 20, md: 30, lg: 40 }}
>
  Content
</Box>
```

When resizing the browser window, the padding values don't follow the expected cascade. For example, at large screen sizes, the padding from smaller breakpoints takes precedence over the `lg` value.

### Expected behavior

Media queries should be sorted from largest to smallest breakpoint so that smaller breakpoints can override larger ones as the viewport shrinks. The `lg` styles should apply at large screens, then be overridden by `md` at medium screens, and so on.

Currently it seems like the order is reversed - smaller breakpoints are being applied first and then larger breakpoints override them, which breaks the responsive behavior.

### System Info
- @mantine/core version: latest
- Browser: tested on Chrome and Firefox

---
Repository: /testbed
