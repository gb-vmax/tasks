# Bug Report

### Describe the bug

The `toggleDirection` function in `DirectionProvider` is causing runtime errors when called. It appears to be trying to access `this.state`, `this.setState`, `this.props`, and `this.updateDependentComponents` which don't exist in the context default value.

### Reproduction

```jsx
import { DirectionContext } from '@mantine/core';

// When using the default context value
const { toggleDirection } = useContext(DirectionContext);

// Calling this throws an error
toggleDirection(); // TypeError: Cannot read property 'state' of undefined
```

The issue occurs when `toggleDirection` is called before a proper `DirectionProvider` is mounted in the component tree. The default context value has a `toggleDirection` function that references `this.state`, `this.props`, and other properties that don't exist.

### Expected behavior

The default `toggleDirection` should either be a no-op function (like it was before) or should handle the case where it's called outside of a provider gracefully without throwing errors.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
