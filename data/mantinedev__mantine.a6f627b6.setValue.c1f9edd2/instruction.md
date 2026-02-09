# Bug Report

### Describe the bug

I'm experiencing a syntax error after the latest update. The application fails to compile with errors about unexpected tokens in the `create-storage.ts` file. It looks like there might be some malformed code that was introduced.

### Reproduction

Just trying to import and use the `useLocalStorage` hook causes the build to fail:

```js
import { useLocalStorage } from '@mantine/hooks';

function MyComponent() {
  const [value, setValue] = useLocalStorage({ key: 'my-key' });
  // Build fails before this even runs
}
```

The error messages point to syntax issues in the storage hook implementation. The code won't even compile, so I can't provide a runtime reproduction.

### Expected behavior

The hook should import and work correctly without compilation errors. This was working fine in the previous version.

### System Info
- @mantine/hooks version: latest
- Build tool: webpack/vite
- Node version: 18.x

---
Repository: /testbed
