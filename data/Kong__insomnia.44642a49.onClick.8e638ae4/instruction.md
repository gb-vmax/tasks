# Bug Report

### Describe the bug

The AsyncButton component is broken after a recent change. It looks like the `onClick` prop definition got accidentally replaced with a function implementation, which breaks the component's type interface.

### Reproduction

```tsx
import { AsyncButton } from './themed-button/async-button';

// This will fail because onClick prop is not properly defined
<AsyncButton
  onClick={async () => {
    await someAsyncOperation();
  }}
>
  Click me
</AsyncButton>
```

### Expected behavior

The AsyncButton should accept an `onClick` prop that takes a function returning a Promise or undefined, and the component should work as intended.

### Additional context

It seems like some code got accidentally committed into the interface definition. The `AsyncButtonProps` interface should define the prop types, not contain function implementations.

---
Repository: /testbed
