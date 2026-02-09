# Bug Report

### Describe the bug

I'm experiencing a syntax error when trying to use the local storage hooks. The application fails to compile with an error about unexpected token `else`.

### Reproduction

```js
import { useLocalStorage } from '@mantine/hooks';

function MyComponent() {
  const [value, setValue] = useLocalStorage({
    key: 'my-key',
    defaultValue: 'initial'
  });

  return (
    <button onClick={() => setValue('updated')}>
      Update Value
    </button>
  );
}
```

When trying to use this component, the build fails immediately. It seems like there's a syntax issue in the storage creation code itself.

### Expected behavior

The hook should work without compilation errors and allow me to set/get values from local storage.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Node version: 18.x

---
Repository: /testbed
