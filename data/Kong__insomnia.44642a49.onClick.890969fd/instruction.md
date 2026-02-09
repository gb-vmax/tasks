# Bug Report

### Describe the bug

There seems to be a syntax error in the `AsyncButton` component that's preventing the application from building. The component definition appears to be malformed with code that looks like it was accidentally pasted into the interface definition.

### Reproduction

```tsx
import { AsyncButton } from './themed-button/async-button';

// Attempting to use AsyncButton results in a build error
<AsyncButton onClick={async () => { /* ... */ }}>
  Click me
</AsyncButton>
```

### Expected behavior

The `AsyncButton` component should compile and render correctly. The interface should properly define the `onClick` prop as a function that accepts a mouse event and returns a Promise or undefined.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
