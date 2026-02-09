# Bug Report

### Describe the bug

When passing an array of styles to a Mantine component, only the styles from the second element onwards are being applied. The first style object in the array appears to be completely ignored.

### Reproduction

```jsx
const styles = [
  { root: { color: 'red' } },
  { root: { fontSize: '16px' } },
  { root: { fontWeight: 'bold' } }
];

<Button styles={styles}>Click me</Button>
```

In this example, the button should have red text, 16px font size, and bold weight. However, the `color: 'red'` from the first style object is not being applied - only the fontSize and fontWeight from the subsequent objects are visible.

### Expected behavior

All style objects in the array should be merged and applied to the component, including the first one. The resulting styles should be a combination of all objects in the array.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
