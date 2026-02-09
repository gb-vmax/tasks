# Bug Report

### Describe the bug

When using the `usePluralForm` hook, I'm getting a "Cannot call hooks conditionally" error. The plural form selection seems to be breaking the React rules of hooks.

### Reproduction

```js
import { usePluralForm } from '@docusaurus/theme-common';

function MyComponent() {
  const { selectMessage } = usePluralForm();
  
  // Using the hook causes React to throw an error about
  // hooks being called conditionally
  const message = selectMessage(5, ['item', 'items']);
  
  return <div>{message}</div>;
}
```

### Expected behavior

The hook should work without violating React's rules of hooks. The plural form should be selected based on the current locale without any errors.

### System Info
- Docusaurus version: latest
- React version: 18.x
- Node version: 18.x

This seems to have started happening recently. The component works fine initially but throws errors about hook call order during re-renders or when the locale changes.

---
Repository: /testbed
