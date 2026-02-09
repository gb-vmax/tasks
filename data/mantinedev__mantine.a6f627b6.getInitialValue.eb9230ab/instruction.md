# Bug Report

### Describe the bug

The `useMediaQuery` hook is not returning the correct initial value during server-side rendering. When passing `initialValue: false` to the hook, it's being ignored and the hook seems to be attempting to access `window.matchMedia` even in SSR environments where `window` is undefined.

### Reproduction

```jsx
// During SSR, this should use the initialValue but doesn't
const matches = useMediaQuery('(min-width: 768px)', false);

// Expected: false (from initialValue)
// Actual: undefined or causes errors
```

The issue appears when:
1. Using the hook in a server-side rendered application (Next.js, Remix, etc.)
2. Providing `initialValue: false` as the second parameter
3. The hook doesn't respect the `false` value and tries to access window APIs

### Expected behavior

When `initialValue` is explicitly set to `false`, the hook should return `false` during SSR instead of trying to access browser APIs. The `initialValue` parameter should work for both `true` and `false` values.

### System Info

- @mantine/hooks version: latest
- Framework: Next.js (SSR enabled)
- Node version: 18.x

---
Repository: /testbed
