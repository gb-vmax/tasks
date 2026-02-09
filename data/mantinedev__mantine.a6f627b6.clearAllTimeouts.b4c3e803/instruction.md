# Bug Report

### Describe the bug

I'm experiencing an issue with transitions where they don't seem to be cleaning up properly. After a component with a transition unmounts, I'm seeing memory leaks and the transition callbacks continue to fire even after the component is gone.

### Reproduction

```jsx
import { Transition } from '@mantine/core';

function MyComponent() {
  const [opened, setOpened] = useState(true);
  
  return (
    <Transition mounted={opened} transition="fade" duration={400}>
      {(styles) => <div style={styles}>Content</div>}
    </Transition>
  );
}

// Steps to reproduce:
// 1. Mount the component with opened={true}
// 2. Quickly toggle opened to false
// 3. Toggle it back to true before the transition completes
// 4. Notice that timeouts/animations aren't being cleared properly
```

### Expected behavior

When a transition is interrupted or the component unmounts, all pending timeouts and animation frames should be properly cleared to prevent memory leaks and unexpected behavior.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
