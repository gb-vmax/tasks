# Bug Report

### Describe the bug

Media queries are being applied in the wrong order when using responsive style props. Styles for larger breakpoints are being overridden by smaller breakpoints, causing responsive layouts to break.

### Reproduction

```jsx
<Box
  w={{ base: '100%', sm: '50%', md: '33%', lg: '25%' }}
>
  Content
</Box>
```

When resizing the browser window, the width doesn't change as expected. For example, at the `lg` breakpoint, the element still has the width from the `base` breakpoint instead of `25%`.

### Expected behavior

Media queries should be sorted from smallest to largest breakpoint so that larger breakpoint styles override smaller ones. The element should display:
- `100%` width on mobile (base)
- `50%` width on small screens (sm)
- `33%` width on medium screens (md)  
- `25%` width on large screens (lg)

### System Info

- @mantine/core version: latest
- Browser: tested on Chrome and Firefox
- OS: macOS

---
Repository: /testbed
