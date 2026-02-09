# Bug Report

### Describe the bug

The `useDocsVersion()` hook is throwing errors or returning incorrect data when used in components. After some investigation, it seems like the hook is trying to access a `docs` property that doesn't exist on the version context object, causing the application to crash or return undefined values.

### Reproduction

```tsx
import { useDocsVersion } from '@docusaurus/theme-common';

function MyComponent() {
  const version = useDocsVersion();
  // version is undefined or has wrong structure
  console.log(version); // Expected: version metadata object
  
  return <div>{version.name}</div>; // Crashes here
}
```

### Expected behavior

The `useDocsVersion()` hook should return the proper version metadata object without accessing non-existent properties. The version data should be returned directly from the context without additional property access.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This seems to have been introduced recently as it was working fine before. The context check condition also looks suspicious - it's checking for `undefined` instead of `null` which might not match how the context is actually initialized.

---
Repository: /testbed
