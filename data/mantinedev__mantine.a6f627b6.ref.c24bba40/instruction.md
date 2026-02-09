# Bug Report

### Describe the bug

I'm experiencing a syntax error when trying to use polymorphic components. It looks like there's a problem with the type definitions in `create-polymorphic-component.ts` that's preventing the code from compiling.

### Reproduction

```tsx
import { createPolymorphicComponent } from '@mantine/core';

const MyComponent = createPolymorphicComponent('div');

// TypeScript compilation fails with syntax error
<MyComponent component="button">
  Click me
</MyComponent>
```

### Expected behavior

The component should compile without errors and allow me to use polymorphic components with the `component` prop or `as` prop to change the underlying element type.

### System Info
- @mantine/core version: latest
- TypeScript version: 4.9+
- React version: 18.x

The error seems to be coming from the type definitions file. It was working fine before the recent update.

---
Repository: /testbed
