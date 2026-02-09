# Bug Report

### Describe the bug
The `Transition` component is not rendering correctly - components that should be visible are not showing up, and the transition animations are not working at all. It seems like the logic for when to show/hide components during transitions has been inverted or broken.

### Reproduction
```jsx
import { Transition } from '@mantine/core';

function Demo() {
  const [mounted, setMounted] = useState(true);
  
  return (
    <>
      <button onClick={() => setMounted((m) => !m)}>Toggle</button>
      <Transition mounted={mounted} transition="fade" duration={400}>
        {(styles) => <div style={styles}>This should fade in/out</div>}
      </Transition>
    </>
  );
}
```

### Expected behavior
- The component should be visible when `mounted` is `true`
- Transitions should animate smoothly when toggling the `mounted` state
- The component should respect the `duration` prop and animate over the specified time

### Actual behavior
- Components are either not visible at all or showing when they shouldn't
- No transition animations are occurring
- The behavior seems completely backwards from what's expected

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

This is blocking our entire UI from working properly since all our modals, popovers, and animated components rely on the Transition component. Any help would be greatly appreciated!

---
Repository: /testbed
