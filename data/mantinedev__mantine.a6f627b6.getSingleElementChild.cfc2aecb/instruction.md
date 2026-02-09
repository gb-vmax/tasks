# Bug Report

### Describe the bug

I'm experiencing an issue with components that expect a single child element. When I pass multiple children, the component is now using the **last child** instead of properly handling the invalid case or using the first child as expected.

### Reproduction

```jsx
import { Tooltip } from '@mantine/core';

// This should either throw an error or use the first child
<Tooltip label="Info">
  <Button>First</Button>
  <Button>Second</Button>
  <Button>Third</Button>
</Tooltip>
```

The tooltip is now attaching to the "Third" button instead of the "First" button or handling this as an invalid case. 

### Expected behavior

When multiple children are provided to a component that expects a single child:
- Either the first valid element child should be used (consistent with previous behavior)
- Or it should return null/handle the invalid case appropriately

Currently it's selecting the last child which seems inconsistent and unexpected.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
