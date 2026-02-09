# Bug Report

### Describe the bug

I'm experiencing a syntax error when trying to use `useLocalStorage` hook. The application fails to compile with a JavaScript parsing error. It seems like there's a malformed code structure in the storage hooks.

### Reproduction

```js
import { useLocalStorage } from '@mantine/hooks';

function MyComponent() {
  const [value, setValue] = useLocalStorage({
    key: 'my-key',
    defaultValue: 'initial'
  });

  return (
    <div>
      <button onClick={() => setValue('updated')}>Update</button>
    </div>
  );
}
```

When trying to build or run the app with this code, I get compilation errors about unexpected tokens or syntax issues.

### Expected behavior

The hook should work without any syntax errors and allow me to store/retrieve values from localStorage.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Node: 18.x

---
Repository: /testbed
