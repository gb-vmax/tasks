# Bug Report

### Describe the bug

The `useLogger` hook is logging mount/unmount messages multiple times when props change. It should only log once on mount and once on unmount, but instead it's re-running the mount effect every time props are updated.

### Reproduction

```jsx
import { useLogger } from '@mantine/hooks';

function MyComponent({ count }) {
  useLogger('MyComponent', [count]);
  return <div>{count}</div>;
}

// When parent updates count prop:
// Expected: Only see "MyComponent updated" logs
// Actual: Seeing "MyComponent unmounted" and "MyComponent mounted" logs on every prop change
```

### Expected behavior

The mount effect should only run once when the component mounts and the cleanup should only run when the component unmounts. Prop changes should only trigger the update logger, not cause remounting logs.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
