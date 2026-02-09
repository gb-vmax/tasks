# Bug Report

### Describe the bug

The `AsyncButton` component has duplicate interface declarations and implementation code, causing TypeScript compilation errors. The component definition appears twice in the file with slightly different signatures.

### Reproduction

When trying to use the `AsyncButton` component:

```tsx
import { AsyncButton } from './themed-button/async-button';

// TypeScript throws errors about duplicate declarations
<AsyncButton
  onClick={async () => {
    await someAsyncOperation();
  }}
  onSuccess={(result) => console.log(result)}
  onError={(error) => console.error(error)}
>
  Click me
</AsyncButton>
```

The file won't compile due to:
- Duplicate `AsyncButtonProps` interface declaration
- Duplicate `AsyncButton` component implementation
- Conflicting type definitions

### Expected behavior

The component should have a single, well-defined interface and implementation. The code should compile without errors and the component should be usable with both the basic `onClick` handler and the new `onSuccess`/`onError` callbacks.

### System Info
- Package: insomnia
- Component: AsyncButton (themed-button)

---
Repository: /testbed
