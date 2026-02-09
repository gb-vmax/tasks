# Bug Report

### Describe the bug

The `useMap` hook's `clear()` method is not working properly. When I call `clear()` on the map returned by `useMap`, it doesn't actually clear the map - the entries remain in the map even after calling clear.

### Reproduction

```js
import { useMap } from '@mantine/hooks';

function MyComponent() {
  const map = useMap([
    ['key1', 'value1'],
    ['key2', 'value2']
  ]);

  const handleClear = () => {
    console.log('Before clear:', map.size); // 2
    map.clear();
    console.log('After clear:', map.size); // Still 2, should be 0
  };

  return (
    <button onClick={handleClear}>Clear Map</button>
  );
}
```

### Expected behavior

After calling `map.clear()`, the map should be empty (size should be 0) and all entries should be removed. The component should also re-render to reflect the cleared state.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
