# Bug Report

### Describe the bug

The `useReactId` hook is returning an empty string when React's `useId` generates a valid ID, and returning a malformed ID when it shouldn't. This causes components that rely on unique IDs to break.

### Reproduction

```jsx
import { useReactId } from '@mantine/hooks';

function MyComponent() {
  const id = useReactId();
  console.log('Generated ID:', id);
  // Expected: "mantine-R1:2:" or similar
  // Actual: "" (empty string)
  
  return <div id={id}>Content</div>;
}
```

When React's `useId()` returns a valid ID like `:R1:`, the hook returns an empty string instead of the expected `mantine-R1` format. This breaks accessibility features and any logic that depends on unique identifiers.

### Expected behavior

The hook should return a properly formatted Mantine ID (e.g., `mantine-R1`) when React's `useId` provides a valid ID, and return an empty string only when no ID is available.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
