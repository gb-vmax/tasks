# Bug Report

### Describe the bug

I'm getting an unexpected error when trying to use `useDocsVersion()` hook in my custom documentation components. The hook is throwing a `ReactContextError` saying 'DocsVersionProvider' even though I'm using it within a proper docs page component that should have the provider available.

### Reproduction

```jsx
import React from 'react';
import { useDocsVersion } from '@docusaurus/theme-common/internal';

function MyCustomComponent() {
  // This throws an error unexpectedly
  const version = useDocsVersion();
  
  return <div>Version: {version.label}</div>;
}
```

When I add this component to a docs page, I get:
```
ReactContextError: DocsVersionProvider
```

### Expected behavior

The `useDocsVersion()` hook should work correctly when used inside docs pages and return the current version metadata without throwing errors. It should only throw the context error when actually used outside of a DocsVersionProvider.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- Browser: Chrome

This seems to have started happening recently. The hook appears to be checking the context incorrectly and throwing errors even when the provider is present.

---
Repository: /testbed
