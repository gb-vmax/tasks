# Bug Report

### Describe the bug

I'm experiencing a syntax error when trying to use the storage hooks (like `useLocalStorage` or `useSessionStorage`). The code fails to compile with errors about unexpected tokens and malformed syntax.

### Reproduction

```js
import { useLocalStorage } from '@mantine/hooks';

function MyComponent() {
  const [value, setValue, removeValue] = useLocalStorage({
    key: 'my-key',
    defaultValue: 'default'
  });

  return (
    <div>
      <button onClick={() => setValue('new value')}>Update</button>
      <button onClick={removeValue}>Remove</button>
    </div>
  );
}
```

### Expected behavior

The hook should work normally and allow setting/removing values from storage without compilation errors.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Build tool: Vite/Webpack

The code was working fine before, but now I'm getting syntax errors when trying to import and use these hooks. It seems like there might be an issue with the package build or source code itself.

---
Repository: /testbed
