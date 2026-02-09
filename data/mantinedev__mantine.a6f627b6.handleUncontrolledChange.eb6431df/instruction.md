# Bug Report

### Describe the bug

The `useUncontrolled` hook is not updating the internal state correctly when used in uncontrolled mode. When the value changes through user interaction, the component displays stale data instead of the new value.

### Reproduction

```jsx
function MyComponent() {
  const [value, handleChange] = useUncontrolled({
    defaultValue: 'initial',
    onChange: (val) => console.log('Changed to:', val)
  });

  return (
    <div>
      <p>Current value: {value}</p>
      <button onClick={() => handleChange('updated')}>
        Update
      </button>
    </div>
  );
}
```

### Expected behavior

When clicking the button, the displayed value should update from 'initial' to 'updated'. The onChange callback fires correctly, but the component still shows 'initial' instead of 'updated'.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
