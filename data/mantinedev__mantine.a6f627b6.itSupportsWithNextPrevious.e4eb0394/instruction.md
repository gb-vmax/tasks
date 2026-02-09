# Bug Report

### Describe the bug

The `withNext` and `withPrevious` props are not working as expected in date picker components. When I set `withNext={false}`, the next button still appears in the UI. Similarly, the previous button shows up even when it shouldn't.

### Reproduction

```jsx
// Next button still appears even when withNext is false
<DatePicker withNext={false} />
// Expected: No next button
// Actual: Next button is still rendered

// Previous button appears when withPrevious is false  
<DatePicker withPrevious={false} />
// Expected: No previous button
// Actual: Previous button is rendered
```

### Expected behavior

When `withNext={false}` is set, the next navigation button should not be rendered.
When `withPrevious={false}` is set, the previous navigation button should not be rendered.

### System Info

- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
