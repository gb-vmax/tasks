# Bug Report

### Describe the bug

I'm experiencing a syntax error when trying to use the `useLocalStorage` hook. The application crashes immediately on import with what appears to be a JavaScript parsing error.

### Reproduction

```js
import { useLocalStorage } from '@mantine/hooks';

function MyComponent() {
  const [value, setValue] = useLocalStorage({
    key: 'my-key',
    defaultValue: 'initial'
  });
  
  return <div>{value}</div>;
}
```

When trying to render this component, I get a syntax error before anything even executes. The error occurs during the module loading phase.

### Expected behavior

The hook should import and work without any syntax errors. The component should render normally with the stored value.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

This seems like it might have been introduced in a recent change? The hook was working fine before updating to the latest version.

---
Repository: /testbed
