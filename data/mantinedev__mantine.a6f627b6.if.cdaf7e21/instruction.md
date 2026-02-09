# Bug Report

### Describe the bug

The `useShallowEffect` hook is not triggering effect callbacks when dependencies change. It seems like the hook is behaving inversely - it runs when dependencies haven't changed and doesn't run when they actually do change.

### Reproduction

```jsx
import { useShallowEffect } from '@mantine/hooks';
import { useState } from 'react';

function MyComponent() {
  const [user, setUser] = useState({ name: 'John', age: 25 });
  
  useShallowEffect(() => {
    console.log('Effect triggered!');
  }, [user]);
  
  // This should trigger the effect, but it doesn't
  const updateUser = () => {
    setUser({ name: 'Jane', age: 30 });
  };
  
  return <button onClick={updateUser}>Update</button>;
}
```

When clicking the button, the effect callback is not executed even though the `user` object reference has changed. However, if I keep clicking without changing the object, the effect randomly triggers.

### Expected behavior

The effect should run when any dependency in the array changes (shallow comparison). In the example above, when `user` changes from `{ name: 'John', age: 25 }` to `{ name: 'Jane', age: 30 }`, the effect should trigger.

Currently it seems to be doing the opposite - running when nothing changes and not running when something does change.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
