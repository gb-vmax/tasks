# Bug Report

### Describe the bug

I'm experiencing an issue where `useMantineContext()` throws an error even when the MantineProvider is properly set up in my component tree. The error message says "MantineProvider was not found in tree" but the provider is definitely there.

### Reproduction

```jsx
import { MantineProvider, useMantineContext } from '@mantine/core';

function MyComponent() {
  const ctx = useMantineContext();
  // Error is thrown here even though MantineProvider wraps this component
  return <div>Test</div>;
}

function App() {
  return (
    <MantineProvider>
      <MyComponent />
    </MantineProvider>
  );
}
```

### Expected behavior

The hook should return the context object when MantineProvider is present in the tree. Instead, it's throwing an error saying the provider wasn't found.

This seems like it might be a regression - it was working fine in earlier versions. The error appears to be thrown unconditionally regardless of whether the provider exists or not.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Node version: 20.x

---
Repository: /testbed
