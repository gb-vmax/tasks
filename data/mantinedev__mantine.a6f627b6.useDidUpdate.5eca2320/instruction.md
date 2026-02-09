# Bug Report

### Describe the bug

The `useDidUpdate` hook is firing on the initial mount instead of only on subsequent updates. It's supposed to skip the first render and only execute the effect callback when dependencies change after the component has mounted, but it's currently running immediately on mount.

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

The callback should only fire when `count` changes after the initial render, not on mount. Currently, the console logs appear immediately when the component first renders, which defeats the purpose of `useDidUpdate` vs regular `useEffect`.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
