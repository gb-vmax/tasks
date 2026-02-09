# Bug Report

### Describe the bug

I'm experiencing an issue with the `classNames` prop when passing an array of class name objects. The styling system seems to be handling arrays incorrectly, causing class names to not be applied properly to components.

### Reproduction

```jsx
import { Button } from '@mantine/core';

const MyComponent = () => {
  return (
    <Button
      classNames={[
        { root: 'custom-class-1' },
        { root: 'custom-class-2' }
      ]}
    >
      Click me
    </Button>
  );
};
```

When passing an array of `classNames` objects like above, the classes are not being applied to the component. It seems like the array is being treated as a single object instead of being properly merged.

### Expected behavior

When providing an array of `classNames` objects, all class names should be merged and applied to the component. Both `custom-class-1` and `custom-class-2` should appear on the root element.

Additionally, when passing a function in the array:

```jsx
classNames={[
  (theme) => ({ root: theme.colorScheme === 'dark' ? 'dark-class' : 'light-class' }),
  { root: 'static-class' }
]}
```

The function should be called and its result merged with the other class names.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
