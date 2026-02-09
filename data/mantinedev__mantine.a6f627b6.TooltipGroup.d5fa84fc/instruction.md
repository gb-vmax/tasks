# Bug Report

### Describe the bug

The `TooltipGroup` component appears to be completely broken. When trying to use it in my application, I get errors about it not being a valid React component.

### Reproduction

```jsx
import { TooltipGroup, Tooltip } from '@mantine/core';

function App() {
  return (
    <TooltipGroup>
      <Tooltip label="First tooltip">
        <button>Hover me</button>
      </Tooltip>
      <Tooltip label="Second tooltip">
        <button>Hover me too</button>
      </Tooltip>
    </TooltipGroup>
  );
}
```

### Expected behavior

The TooltipGroup should wrap multiple tooltips and coordinate their opening/closing delays as documented. Instead, the component doesn't render anything and throws errors.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
