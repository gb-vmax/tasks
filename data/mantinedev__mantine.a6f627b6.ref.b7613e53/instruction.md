# Bug Report

### Describe the bug

The `createPolymorphicComponent` function appears to be broken. When trying to use polymorphic components, I'm getting TypeScript errors and the components fail to render properly. It looks like the type definitions got corrupted or mixed with implementation code.

### Reproduction

```tsx
import { createPolymorphicComponent } from '@mantine/core';

const MyComponent = createPolymorphicComponent('div');

// TypeScript errors when trying to use the component
function App() {
  return <MyComponent component="button">Click me</MyComponent>;
}
```

### Expected behavior

The polymorphic component should:
1. Accept a `component` prop to change the rendered element
2. Properly forward refs
3. Support the `renderRoot` option for custom rendering
4. Have correct TypeScript types

### Current behavior

Getting TypeScript compilation errors and the component doesn't work as expected. The type definition for `PolymorphicComponentProps` seems malformed - it looks like function implementation code got inserted into the type definition itself.

### System Info

- @mantine/core version: latest
- React version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
