# Bug Report

### Describe the bug

When using `withProps()` on a Mantine component, the component crashes with a syntax error. It looks like there's an issue with how the `withProps` method is defined in the factory.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// This throws an error
const CustomButton = Button.withProps({
  variant: 'filled',
  color: 'blue'
});

function App() {
  return <CustomButton>Click me</CustomButton>;
}
```

### Expected behavior

The component should render successfully with the default props applied. The `withProps` utility should allow creating component variants with pre-configured props.

### Error

The code fails to parse/compile. It seems like the factory type definition is malformed.

### System Info

- @mantine/core version: latest
- React version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
