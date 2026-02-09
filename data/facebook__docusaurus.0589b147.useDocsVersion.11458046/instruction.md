# Bug Report

### Describe the bug

I'm encountering an issue where using `useDocsVersion()` hook throws an error even when the hook is properly wrapped with `DocsVersionProvider`. The error message says the provider is missing, but it's actually present in the component tree.

### Reproduction

```jsx
import { DocsVersionProvider, useDocsVersion } from '@docusaurus/theme-common';

function MyComponent() {
  const version = useDocsVersion();
  return <div>{version.name}</div>;
}

function App() {
  const versionMetadata = {
    name: 'current',
    label: 'Next',
    // ... other metadata
  };
  
  return (
    <DocsVersionProvider version={versionMetadata}>
      <MyComponent />
    </DocsVersionProvider>
  );
}
```

### Expected behavior

The component should render without errors and be able to access the version metadata from the context.

### Actual behavior

The application throws a ReactContextError indicating that `DocsVersionProvider` is missing, even though it's clearly wrapping the component that calls `useDocsVersion()`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
