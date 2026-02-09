# Bug Report

### Describe the bug

The `useLogger` hook is not logging prop updates correctly. When props change, the logger shows stale values instead of the current ones. The mount and unmount messages also don't reflect the current component name if it changes.

### Reproduction

```jsx
function TestComponent({ value }) {
  useLogger('MyComponent', [value]);
  return <div>{value}</div>;
}

// Render with initial value
<TestComponent value="initial" />

// Update the prop
<TestComponent value="updated" />
```

When the prop changes from "initial" to "updated", the console log shows the old value instead of the new one. Similarly, if the component name were to change dynamically, the unmount message would show the old name.

### Expected behavior

The logger should display the current prop values when they update, not stale values from the previous render. The mount/unmount messages should also use the current component name.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
