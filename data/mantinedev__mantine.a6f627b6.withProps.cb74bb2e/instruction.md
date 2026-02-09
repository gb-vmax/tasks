# Bug Report

### Describe the bug

The `withProps` method is not accepting partial props anymore. When trying to pass a subset of component props to `withProps`, TypeScript throws an error saying that required properties are missing.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// This used to work but now fails with TypeScript error
const StyledButton = Button.withProps({
  color: 'blue',
  // size is required but we only want to override color
});

// Error: Property 'children' is required but not provided
```

Previously, `withProps` would accept partial props and allow you to override only specific properties while leaving others to be provided when the component is used. Now it seems to require all props to be provided upfront.

### Expected behavior

`withProps` should accept partial props so that you can create component variants by overriding only specific properties. The remaining props should still be passable when actually rendering the component.

```tsx
const StyledButton = Button.withProps({
  color: 'blue'
});

// Should be able to use it like this
<StyledButton>Click me</StyledButton>
```

### System Info
- @mantine/core version: latest
- TypeScript version: 5.x

---
Repository: /testbed
