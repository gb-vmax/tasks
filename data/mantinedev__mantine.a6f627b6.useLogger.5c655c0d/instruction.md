# Bug Report

### Describe the bug

The `useLogger` hook is not behaving correctly after a recent update. It's supposed to log component lifecycle events, but the unmount logging isn't working and prop updates aren't being tracked properly.

### Reproduction

```jsx
import { useLogger } from '@mantine/hooks';

function MyComponent({ count, name }) {
  useLogger('MyComponent', [count, name]);
  
  return <div>{count} - {name}</div>;
}

// Usage:
// 1. Mount component with count=0, name="test"
// 2. Update props to count=1, name="test" 
// 3. Unmount component
```

### Expected behavior

- On mount: Should log "MyComponent mounted" with initial props
- On prop update: Should log "MyComponent updated" with new props when count or name changes
- On unmount: Should log "MyComponent unmounted" when component is removed

### Actual behavior

- Unmount message appears immediately on mount instead of when component unmounts
- Prop updates are not being logged at all, even when the props change

This makes it impossible to properly debug component lifecycle with this hook.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
