# Bug Report

### Popover toggle not working when disabled prop is explicitly set to false

I'm experiencing an issue with the Popover component where the toggle functionality behaves incorrectly when the `disabled` prop is explicitly set to `false`.

### Reproduction

```jsx
import { Popover } from '@mantine/core';

function MyComponent() {
  return (
    <Popover disabled={false}>
      <Popover.Target>
        <button>Toggle</button>
      </Popover.Target>
      <Popover.Dropdown>
        Content here
      </Popover.Dropdown>
    </Popover>
  );
}
```

When clicking the toggle button, the popover doesn't open/close as expected. If I remove the `disabled={false}` prop entirely, it works fine.

### Expected behavior

Setting `disabled={false}` explicitly should behave the same as not setting the disabled prop at all - the popover should toggle normally when clicking the target element.

### Additional context

This seems to only happen when the disabled prop is explicitly passed as `false`. When the prop is omitted or set to `true`, the behavior is as expected.

---
Repository: /testbed
