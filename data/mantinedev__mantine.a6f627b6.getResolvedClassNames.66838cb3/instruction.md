# Bug Report

### Describe the bug
When using the Styles API with custom selectors, the class names are not being resolved correctly. It seems like the selector resolution logic is broken - instead of returning the class name for the requested selector, it's attempting to access nested properties that don't exist, resulting in `undefined` being returned.

### Reproduction
```jsx
import { useStyles } from '@mantine/core';

const MyComponent = () => {
  const { classes } = useStyles({
    classNames: {
      root: 'my-root-class',
      label: 'my-label-class'
    }
  });

  // classes.root returns undefined instead of 'my-root-class'
  return <div className={classes.root}>Content</div>;
}
```

### Expected behavior
The `classes` object should contain the resolved class names for each selector. When accessing `classes.root`, it should return the appropriate class name string, not `undefined`.

### System Info
- @mantine/core version: latest
- React version: 18.x

This appears to have started happening recently. The Styles API was working fine before but now components aren't receiving their proper class names.

---
Repository: /testbed
