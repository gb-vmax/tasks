# Bug Report

### Describe the bug

The `useDocsVersion()` hook is throwing an error when it's actually being used correctly within a `DocsVersionProvider`. The error message says "DocsVersion context is available" even though the context should be working normally.

### Reproduction

```jsx
import { DocsVersionProvider, useDocsVersion } from '@docusaurus/theme-common';

function MyComponent() {
  // This throws an error even though we're inside the provider
  const version = useDocsVersion();
  return <div>{version.name}</div>;
}

function App() {
  return (
    <DocsVersionProvider version={someVersionMetadata}>
      <MyComponent />
    </DocsVersionProvider>
  );
}
```

### Expected behavior

The hook should return the version metadata without throwing an error when used inside a `DocsVersionProvider`. It should only throw an error when the context is NOT available (i.e., when used outside the provider).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
