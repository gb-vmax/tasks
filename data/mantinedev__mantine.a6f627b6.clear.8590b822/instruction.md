# Bug Report

### Describe the bug

The `useSet` hook's `clear()` method is causing issues - when I call `clear()` on the set, it triggers a re-render but the set isn't actually cleared. The UI updates as if the set is empty, but the underlying set still contains all the elements.

### Reproduction

```js
import { useSet } from '@mantine/hooks';

function MyComponent() {
  const mySet = useSet(['item1', 'item2', 'item3']);
  
  const handleClear = () => {
    mySet.clear();
    console.log('Set size after clear:', mySet.size); // Expected: 0, Actual: 3
    console.log('Set has item1:', mySet.has('item1')); // Expected: false, Actual: true
  };
  
  return (
    <div>
      <p>Set size: {mySet.size}</p>
      <button onClick={handleClear}>Clear Set</button>
    </div>
  );
}
```

### Expected behavior

After calling `clear()`, the set should be empty (size = 0) and subsequent calls to `has()` should return false for all previously added items. The component should re-render showing the empty set.

### Actual behavior

The component re-renders (the UI updates), but the set is not actually cleared. Checking the size or using `has()` shows that all elements are still present in the set.

---
Repository: /testbed
