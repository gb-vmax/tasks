# Bug Report

### Describe the bug

The `useShallowEffect` hook is not triggering effects properly when dependencies change. It seems like the effect callback is being called even when the dependencies haven't actually changed, or conversely, not being called when they should be.

### Reproduction

```jsx
import { useShallowEffect } from '@mantine/hooks';
import { useState } from 'react';

function MyComponent() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([1, 2, 3]);

  useShallowEffect(() => {
    console.log('Effect triggered');
  }, [items]);

  // When updating items to a new array with same values
  // the effect should trigger, but it doesn't behave as expected
  const handleClick = () => {
    setItems([1, 2, 3]); // New array, same values
  };

  return <button onClick={handleClick}>Update</button>;
}
```

### Expected behavior

The hook should perform a shallow comparison of dependencies and only trigger the effect when the dependencies have actually changed at a shallow level. Currently it's not comparing dependencies correctly.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
