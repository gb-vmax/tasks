# Bug Report

### Describe the bug

The clear button is not appearing when the `clearable` prop is set to `true` on date components. Even though I'm passing `clearable` and `clearButtonProps`, the clear button is not being rendered in the component.

### Reproduction

```jsx
<DatePicker
  clearable
  clearButtonProps={{ 'aria-label': 'clear-date' }}
  rightSection={<span>Custom section</span>}
/>
```

When I check the DOM, I can't find the clear button element even though `clearable` is explicitly set to `true`. The right section renders correctly, but the clear button is missing.

### Expected behavior

When `clearable` is set to `true`, a clear button should be rendered in the component with the provided `clearButtonProps`. The button should be accessible via its aria-label.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
