# Bug Report

### Describe the bug

I'm getting a syntax error when trying to use the modals package. The application fails to compile/build with an error related to the `events.ts` file in `@mantine/modals`.

### Reproduction

```tsx
import { modals } from '@mantine/modals';

// Trying to open a modal
modals.openModal({
  title: 'Test Modal',
  children: <div>Content</div>,
});
```

When I try to run this code, the build fails immediately. It seems like there's a syntax issue in the type definitions or the events file itself.

### Expected behavior

The modal should open without any compilation errors. The `openModal` function should be callable and return a modal ID string.

### System Info
- @mantine/modals version: latest
- React version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
