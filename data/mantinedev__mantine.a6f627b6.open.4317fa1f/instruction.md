# Bug Report

### Describe the bug

After a recent update, the `useModalsStack` hook appears to be broken. When trying to use it in my application, I'm getting TypeScript errors and the modals aren't functioning at all. It looks like the hook's return type and implementation got corrupted somehow.

### Reproduction

```tsx
import { useModalsStack } from '@mantine/core';

function MyComponent() {
  const modals = useModalsStack(['login', 'signup']);
  
  // Trying to open a modal
  modals.open('login'); // This doesn't work anymore
  
  return (
    <div>
      {/* Modal components */}
    </div>
  );
}
```

### Expected behavior

The hook should return an object with `open`, `close`, `toggle`, `closeAll`, and `register` methods that work with the modal stack. The state should track which modals are open.

### Additional context

Looking at the source code, it seems like there's some Svelte-specific code (`writable`, `derived`) that got mixed into the React implementation. The function signature is also malformed - there's an `export function` declaration inside the interface definition which doesn't make sense.

This is completely breaking my modal functionality. The hook used to work fine before this change.

---
Repository: /testbed
