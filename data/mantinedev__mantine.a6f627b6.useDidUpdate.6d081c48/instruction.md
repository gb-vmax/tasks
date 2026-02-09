# Bug Report

### Describe the bug

The `useDidUpdate` hook is triggering on the initial mount instead of only on subsequent updates. The callback function is being executed immediately when the component first renders, which defeats the purpose of having a "didUpdate" hook that should skip the initial mount.

### Reproduction

```jsx
import { useDidUpdate } from '@mantine/hooks';
import { useState } from 'react';

function MyComponent() {
  const [count, setCount] = useState(0);

  useDidUpdate(() => {
    console.log('This should NOT log on initial mount');
    console.log('Count updated:', count);
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### Expected behavior

The callback should only execute when dependencies change AFTER the initial mount. On the first render, nothing should be logged to the console. The message should only appear when clicking the increment button.

### Actual behavior

The callback executes immediately on mount, logging the message even though no update has occurred yet. This is the same behavior as a regular `useEffect` hook, making `useDidUpdate` not work as intended.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
