# Bug Report

### Describe the bug

The Collapse component is not working correctly when the element ref is null or undefined. Instead of falling back to 'auto' height, it's now returning 0, which causes the collapse animation to not work properly.

### Reproduction

```jsx
import { Collapse } from '@mantine/core';

function MyComponent() {
  const [opened, setOpened] = useState(false);
  
  return (
    <>
      <button onClick={() => setOpened(!opened)}>Toggle</button>
      <Collapse in={opened}>
        <div>Content that should collapse</div>
      </Collapse>
    </>
  );
}
```

When toggling the collapse, the content doesn't animate properly. It seems like the height calculation is returning 0 instead of 'auto' when the element reference is not available.

### Expected behavior

The Collapse component should handle cases where the element ref is null/undefined by falling back to 'auto' height, allowing the content to expand/collapse smoothly.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
