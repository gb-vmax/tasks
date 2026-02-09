# Bug Report

### Describe the bug

The `extend` static function is not being detected properly on components. When checking if a component has the `extend` method, it appears to be looking at the wrong property, causing the validation to fail.

### Reproduction

```tsx
import { MyComponent } from '@mantine/core';

// Component should have extend method
console.log(typeof MyComponent.extend); // Expected: 'function', Actual: undefined
```

When trying to use the `extend` function on any Mantine component, it's not recognized even though components are supposed to have this static method available.

### Expected behavior

Components should have a static `extend` function that can be called to customize component behavior. The type check should correctly identify this function as existing.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
