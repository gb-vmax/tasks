# Bug Report

### Describe the bug

After a recent update, I'm getting syntax errors when trying to use `useLocalStorage` or any of the storage hooks. The code won't compile and throws errors about unexpected tokens.

### Reproduction

```jsx
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

When trying to build or run this code, I get compilation errors. The hook itself seems to have syntax issues in the source code.

### Expected behavior

The hook should work without any syntax errors and allow me to store/retrieve values from localStorage as before.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Build tool: Vite

---
Repository: /testbed
