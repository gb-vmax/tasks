# Bug Report

### Describe the bug

I'm experiencing an issue with `useShallowEffect` where the effect callback is not firing correctly when dependencies change. The hook seems to be detecting changes in an inverted way - it triggers when values are equal and doesn't trigger when they actually change.

### Reproduction

```js
import { useShallowEffect } from '@mantine/hooks';

function MyComponent() {
  const [count, setCount] = useState(0);
  const [data, setData] = useState({ value: 1 });

  useShallowEffect(() => {
    console.log('Effect triggered');
  }, [count, data]);

  // When clicking this button, the effect doesn't trigger even though count changed
  return (
    <button onClick={() => setCount(count + 1)}>
      Increment
    </button>
  );
}
```

### Expected behavior

The effect should trigger when any dependency in the array changes (shallow comparison). Currently it seems like the comparison logic is backwards - the effect runs when dependencies haven't changed and doesn't run when they have changed.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
