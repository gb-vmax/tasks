# Bug Report

### Describe the bug

After a recent update, I'm getting a TypeScript error when trying to use the `extend` method on Mantine components. The error says that `extend` is not a function, even though the type definition suggests it should be.

### Reproduction

```tsx
import { factory } from '@mantine/core';

const MyComponent = factory((props) => {
  return <div>Test</div>;
});

// This throws: "extend is not a function"
const ExtendedComponent = MyComponent.extend({
  defaultProps: {
    size: 'md'
  }
});
```

### Expected behavior

The `extend` method should be callable and return a new component with the extended configuration merged with the original component's configuration.

### System Info
- @mantine/core version: latest
- TypeScript: 5.x
- React: 18.x

---
Repository: /testbed
