# Bug Report

### Describe the bug

After a recent update, the `AsyncButton` component seems to have a syntax/structural issue. The component is not rendering and appears to be completely broken. When trying to use any button that relies on `AsyncButton`, the application fails to work properly.

### Reproduction

```tsx
import { AsyncButton } from './themed-button/async-button';

// Try to use AsyncButton in any component
<AsyncButton 
  onClick={async () => {
    await someAsyncOperation();
  }}
>
  Click Me
</AsyncButton>
```

The button doesn't render at all and the component seems malformed.

### Expected behavior

The `AsyncButton` should render normally and handle async click operations as it did before. The component should accept an `onClick` prop that returns a Promise and handle loading states appropriately.

### Additional context

This seems to have broken suddenly - the button component was working fine previously. Looking at the component file, something seems off with the interface definition but I can't pinpoint exactly what's wrong.

---
Repository: /testbed
