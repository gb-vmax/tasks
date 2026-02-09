# Bug Report

### Describe the bug

Media queries are being applied in the wrong order when using responsive style props. Instead of applying from smallest to largest breakpoint (mobile-first approach), they seem to be reversed or incorrectly sorted, causing larger breakpoint styles to be overridden by smaller ones.

### Reproduction

```jsx
<Box
  p={{ base: 10, sm: 20, md: 30, lg: 40 }}
>
  Content
</Box>
```

When inspecting the generated CSS, the media queries appear in an unexpected order. The styles that should apply at larger breakpoints are being overridden by smaller breakpoint styles because they're appearing in the wrong sequence in the stylesheet.

### Expected behavior

Media queries should be sorted from smallest to largest breakpoint values to follow a mobile-first approach. Styles defined for larger breakpoints should override those for smaller breakpoints, not the other way around.

For example, if I set padding of 10 for base, 20 for sm, and 30 for md, at the md breakpoint I should see padding of 30, not 10 or 20.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
