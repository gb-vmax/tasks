# Bug Report

### Describe the bug

The `AsyncButton` component appears to have duplicate code in its implementation. When trying to use the component, TypeScript throws errors about duplicate identifiers and the component doesn't render correctly.

### Reproduction

```tsx
import { AsyncButton } from './async-button';

// Attempting to use the component
<AsyncButton
  onClick={async () => {
    await someAsyncOperation();
  }}
>
  Click me
</AsyncButton>
```

The component fails to compile and TypeScript reports errors about duplicate property declarations in the `AsyncButtonProps` interface.

### Expected behavior

The `AsyncButton` component should compile without errors and render properly. The `onClick` prop should accept either a simple async handler or a configuration object with `handler`, `onSuccess`, and `onError` callbacks.

### Additional context

It looks like there might be some duplicated code in the component definition - the `onClick` property type appears to be defined twice in the interface, and the `isCallbackConfig` function seems to be placed inside the interface definition instead of outside it.

---
Repository: /testbed
