# Bug Report

### Describe the bug

I'm getting an error when trying to use `useMantineTheme()` hook inside a component that's properly wrapped with `MantineProvider`. The error message says "MantineProvider was not found in component tree" even though the provider is clearly present in my app structure.

### Reproduction

```jsx
import { MantineProvider, useMantineTheme } from '@mantine/core';

function MyComponent() {
  const theme = useMantineTheme();
  return <div>{theme.colorScheme}</div>;
}

function App() {
  return (
    <MantineProvider>
      <MyComponent />
    </MantineProvider>
  );
}
```

Running this code throws an error:
```
Error: @mantine/core: MantineProvider was not found in component tree, make sure you have it in your app
```

### Expected behavior

The `useMantineTheme()` hook should return the theme object without throwing an error when used inside a component that's wrapped with `MantineProvider`.

### Additional context

This seems to have started happening recently. The same code was working fine before. I've double-checked my component tree and the MantineProvider is definitely wrapping the component that uses the hook.

---
Repository: /testbed
