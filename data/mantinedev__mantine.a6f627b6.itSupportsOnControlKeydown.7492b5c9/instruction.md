# Bug Report

### Describe the bug

The `onControlKeydown` callback is not being triggered when pressing Enter key on date picker controls. It seems like the keyboard event handling might have changed or there's an issue with how the Enter key is being processed.

### Reproduction

```jsx
<DatePicker
  onControlKeydown={(event) => {
    console.log('Key pressed:', event);
  }}
/>
```

Steps to reproduce:
1. Render a date picker component with `onControlKeydown` prop
2. Focus on a date control button
3. Press the Enter key
4. The callback is not invoked

### Expected behavior

The `onControlKeydown` callback should be triggered when pressing Enter on date picker control buttons, similar to how it works with other keyboard interactions like Space key.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
