# Bug Report

### Describe the bug

When using the `Box` component with both `style` and `vars` props, the custom styles passed through the `style` prop are not being applied. It seems like the `vars` are overriding the `style` prop instead of both being merged correctly.

### Reproduction

```jsx
<Box
  style={{ backgroundColor: 'red', padding: '20px' }}
  vars={{ '--custom-color': 'blue' }}
>
  Content here
</Box>
```

The background color and padding from the `style` prop don't appear in the rendered component. Only the CSS variables from `vars` are applied.

### Expected behavior

Both the `style` prop and `vars` should be merged and applied to the component. The custom styles shouldn't be lost when CSS variables are also provided.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
