# Bug Report

### Describe the bug

After a recent update, the `AsyncButton` component appears to have duplicate interface definitions and implementation code in the source file. The component seems to be defined twice, which is causing issues when trying to use the component.

### Reproduction

When trying to import and use `AsyncButton`:

```tsx
import { AsyncButton } from './themed-button/async-button';

// Component usage
<AsyncButton onClick={handleClick}>
  Click me
</AsyncButton>
```

The component behavior is unpredictable - sometimes the new `onSuccess` and `onError` callbacks work, sometimes they don't. Looking at the source code, it seems like there are two complete definitions of both the interface and the component implementation.

### Expected behavior

The component should have a single, clean interface definition and implementation. The `AsyncButton` should work consistently with its props including the callback handlers.

### System Info
- Insomnia version: latest
- OS: N/A (source code issue)

---
Repository: /testbed
