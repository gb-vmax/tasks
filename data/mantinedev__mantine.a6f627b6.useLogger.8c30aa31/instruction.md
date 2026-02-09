# Bug Report

### Describe the bug

The `useLogger` hook is not logging component updates correctly. When props change, the hook logs the mount/unmount instead of the update, and when the component actually updates, it's not capturing the current prop values.

### Reproduction

```jsx
import { useLogger } from '@mantine/hooks';

function MyComponent({ count, name }) {
  useLogger('MyComponent', [count, name]);
  
  return <div>{count} - {name}</div>;
}

// Usage:
// 1. Initial render with count=0, name="test"
//    Expected: "MyComponent mounted 0 test"
//    Actual: Works correctly
//
// 2. Update count to 1
//    Expected: "MyComponent updated 1 test"
//    Actual: "MyComponent unmounted" and "MyComponent mounted 1 test" are logged instead
//
// 3. Update name to "updated" 
//    Expected: "MyComponent updated 1 updated"
//    Actual: The update log shows stale prop values
```

### Expected behavior

- When props change, `useLogger` should log "ComponentName updated" with the current prop values
- Mount/unmount should only be logged when the component actually mounts/unmounts, not on every prop change
- The update logs should always show the current prop values, not stale ones

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
