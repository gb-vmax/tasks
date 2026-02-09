# Bug Report

### Describe the bug

After a recent update, the `AsyncButton` component appears to have duplicate interface definitions and implementation code. The component's TypeScript interface `AsyncButtonProps` is defined twice, and the component implementation itself seems to be duplicated as well. This is causing compilation errors when trying to build the project.

### Reproduction

```tsx
import { AsyncButton } from '@/ui/components/themed-button/async-button';

// Attempting to use the component results in build errors
<AsyncButton
  onClick={async () => {
    await someAsyncOperation();
  }}
>
  Click me
</AsyncButton>
```

### Expected behavior

The component should have a single, clean interface definition and implementation. The code should compile without errors.

### System Info
- Package: insomnia
- Component: themed-button/async-button.tsx

The file seems to have merge conflict remnants or accidental duplication. The interface properties like `errorNode`, `onSuccess`, and `onError` appear to be defined but then the old interface definition is repeated below.

---
Repository: /testbed
