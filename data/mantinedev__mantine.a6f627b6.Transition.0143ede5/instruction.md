# Bug Report

### Describe the bug

The `Transition` component is displaying content at the wrong times - it shows when it should be hidden and hides when it should be visible. This appears to be affecting both the initial mount state and the transition status checks.

### Reproduction

```jsx
import { Transition } from '@mantine/core';

function App() {
  const [mounted, setMounted] = useState(true);
  
  return (
    <div>
      <button onClick={() => setMounted(!mounted)}>Toggle</button>
      <Transition mounted={mounted} transition="fade" duration={300}>
        {(styles) => <div style={styles}>This should be visible when mounted=true</div>}
      </Transition>
    </div>
  );
}
```

### Expected behavior

- When `mounted={true}`, the content should be visible
- When `mounted={false}`, the content should be hidden (or not rendered if `keepMounted` is false)
- During transitions, the content should appear/disappear smoothly

### Current behavior

The component is showing the opposite behavior - content appears when it should be hidden and vice versa. This makes the transition completely backwards.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
