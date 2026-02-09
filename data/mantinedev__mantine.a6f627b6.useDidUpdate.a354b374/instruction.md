# Bug Report

### Describe the bug

The `useDidUpdate` hook is firing on the initial mount instead of only on subsequent updates. It's supposed to skip the first render and only execute the callback on dependency changes after mount, but it's currently running immediately when the component first renders.

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
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}
```

### Expected behavior

The callback should only execute when dependencies change AFTER the initial mount. On first render, nothing should be logged. The console message should only appear when clicking the increment button.

### Actual behavior

The callback executes immediately on mount, logging the message even before any user interaction.

This breaks the intended behavior where `useDidUpdate` should be equivalent to `componentDidUpdate` in class components - only running after updates, not on initial mount.

---
Repository: /testbed
