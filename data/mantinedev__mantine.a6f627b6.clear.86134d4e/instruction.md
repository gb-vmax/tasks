# Bug Report

### Describe the bug
When using the `useSet` hook, calling the `clear()` method doesn't actually clear the set. The set still contains all its elements after calling `clear()`, even though the component re-renders.

### Reproduction
```js
import { useSet } from '@mantine/hooks';

function MyComponent() {
  const mySet = useSet(['item1', 'item2', 'item3']);
  
  const handleClear = () => {
    mySet.clear();
    console.log(mySet.size); // Expected: 0, Actual: 3
    console.log([...mySet]); // Still contains all items
  };
  
  return <button onClick={handleClear}>Clear Set</button>;
}
```

### Expected behavior
After calling `clear()`, the set should be empty with size 0 and contain no elements.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
