# Bug Report

### Describe the bug
The `useMap` hook's `clear()` method doesn't actually clear the map anymore. After calling `clear()` on the map returned by `useMap`, all the entries remain in the map instead of being removed.

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

  return <button onClick={handleClear}>Clear Map</button>;
}
```

### Expected behavior
After calling `map.clear()`, the map should be empty and `map.size` should return 0. The component should also re-render to reflect the cleared state.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

This seems like a regression as it was working fine before. The map still triggers a re-render but the actual clear operation doesn't happen.

---
Repository: /testbed
