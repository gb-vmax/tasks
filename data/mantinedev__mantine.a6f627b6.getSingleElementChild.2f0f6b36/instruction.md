# Bug Report

### Describe the bug

When using components that wrap a single child element, passing multiple children now causes the wrapper to render the first child instead of returning `null` as expected. This breaks the intended validation behavior where components should only accept exactly one child element.

### Reproduction

```jsx
import { Tooltip } from '@mantine/core';

// This should not work but now renders the first button
<Tooltip label="Info">
  <button>First</button>
  <button>Second</button>
</Tooltip>
```

The component accepts multiple children and just uses the first one, when it should reject the invalid prop configuration entirely.

### Expected behavior

Components that are designed to wrap a single child element should return `null` or throw an error when multiple children are provided, not silently accept the first child and ignore the rest.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
