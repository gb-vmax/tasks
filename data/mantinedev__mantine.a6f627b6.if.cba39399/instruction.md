# Bug Report

### Describe the bug

The `useShallowEffect` hook is not triggering effects on initial mount when dependencies are provided. The effect callback doesn't execute even though dependencies are present and valid.

### Reproduction

```js
import { useShallowEffect } from '@mantine/hooks';

function MyComponent() {
  useShallowEffect(() => {
    console.log('Effect triggered');
    // This should run on mount but doesn't
  }, [{ key: 'value' }]);

  return <div>Test</div>;
}
```

### Expected behavior

The effect should run on the initial mount when dependencies are provided, similar to how `useEffect` behaves. Currently, the effect callback is not being called at all on first render.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
