# Bug Report

### Describe the bug

The `useShallowEffect` hook is triggering unexpectedly when both the previous and current dependency lists are `null` or `undefined`. This causes the effect to run even when there are no actual changes to the dependencies.

### Reproduction

```jsx
import { useShallowEffect } from '@mantine/hooks';

function MyComponent() {
  const [count, setCount] = useState(0);
  
  useShallowEffect(() => {
    console.log('Effect triggered');
    // This runs on every render when dependencies are null/undefined
  }, null);
  
  return <button onClick={() => setCount(count + 1)}>Click me</button>;
}
```

When clicking the button, the effect runs on every render even though the dependencies haven't changed (both are `null`).

### Expected behavior

When both the previous and current dependency lists are `null` or `undefined`, the hook should recognize them as equal and not trigger the effect unnecessarily. The effect should only run when there's an actual change in dependencies.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
