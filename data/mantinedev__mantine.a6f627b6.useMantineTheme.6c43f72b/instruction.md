# Bug Report

### Describe the bug

I'm getting an error when trying to use `useMantineTheme()` hook in my components even though I have `MantineProvider` properly set up in my app tree. The error message says "MantineProvider was not found in component tree" but I can confirm it's definitely there.

### Reproduction

```jsx
import { MantineProvider, useMantineTheme } from '@mantine/core';

function App() {
  return (
    <MantineProvider>
      <MyComponent />
    </MantineProvider>
  );
}

function MyComponent() {
  const theme = useMantineTheme(); // This throws an error
  
  return <div>Component content</div>;
}
```

### Expected behavior

The `useMantineTheme()` hook should return the theme object when called inside a component that's wrapped with `MantineProvider`. It shouldn't throw an error about the provider not being found when it clearly exists in the component tree.

### Additional context

This was working fine before, but after updating to the latest version it started throwing this error consistently. The `MantineProvider` is definitely in the tree and other Mantine components render correctly, but accessing the theme via the hook fails.

---
Repository: /testbed
