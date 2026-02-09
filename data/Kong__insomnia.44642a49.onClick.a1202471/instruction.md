# Bug Report

### Describe the bug

I'm encountering a syntax error in the `AsyncButton` component after a recent update. The component appears to have malformed TypeScript interface definition that's preventing the application from compiling.

### Reproduction

When trying to use the `AsyncButton` component:

```tsx
import { AsyncButton } from '@/ui/components/themed-button/async-button';

<AsyncButton
  onClick={async () => {
    await someAsyncOperation();
  }}
>
  Click Me
</AsyncButton>
```

The build fails with a TypeScript compilation error. It looks like there's an issue with the interface definition for `AsyncButtonProps` where the `onClick` prop is not properly defined.

### Expected behavior

The `AsyncButton` component should accept an `onClick` prop that can be either an async function returning a Promise or undefined, and the component should compile without errors.

### System Info
- Insomnia version: latest
- Node version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
