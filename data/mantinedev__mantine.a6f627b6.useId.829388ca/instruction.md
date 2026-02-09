# Bug Report

### Describe the bug

The `useId` hook is returning incorrect ID values. When a `staticId` is provided, it's being ignored and a generated ID is returned instead. Additionally, during server-side rendering, the hook returns a different ID than what's expected.

### Reproduction

```jsx
import { useId } from '@mantine/hooks';

function MyComponent() {
  // Expected: 'my-custom-id'
  // Actual: Returns a generated react ID instead
  const id1 = useId('my-custom-id');
  
  console.log(id1); // Should be 'my-custom-id' but returns something else
  
  return <div id={id1}>Content</div>;
}
```

For SSR scenario:
```jsx
// During server-side rendering
const id = useId();
// Expected: React's useId value
// Actual: Returns uuid instead
```

### Expected behavior

1. When a `staticId` parameter is passed to `useId`, it should return that exact static ID
2. During server-side rendering (when `window` is undefined), it should return the React-generated ID for consistency
3. Only in the browser without a static ID should it return the uuid

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Environment: Both browser and SSR

---
Repository: /testbed
