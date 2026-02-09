# Bug Report

### Describe the bug

The `AsyncButton` component is not rendering properly - it seems like the component definition got mangled and the interface properties are appearing in the wrong place. When trying to use the component, I'm getting TypeScript errors about the structure.

### Reproduction

```tsx
import { AsyncButton } from './async-button';

// Trying to use the component
<AsyncButton
  onClick={async () => {
    await someAsyncOperation();
  }}
  loadingNode={<Spinner />}
>
  Click me
</AsyncButton>
```

The component doesn't render and TypeScript complains about the prop types being malformed.

### Expected behavior

The `AsyncButton` should render normally and accept the standard props like `onClick`, `loadingNode`, `onSuccess`, `onError`, etc. The interface definition should be properly separated from the component implementation.

### System Info
- Insomnia version: latest
- Node version: 18.x

This looks like maybe a merge conflict or copy-paste error got committed? The interface properties seem to be mixed into the middle of the component code.

---
Repository: /testbed
