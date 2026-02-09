# Bug Report

### Accordion panels showing/hiding in reverse

I'm experiencing a strange issue with the Accordion component where the panels are behaving opposite to what they should. When I click to expand an accordion item, it collapses instead, and when I click to collapse it, it expands.

### Reproduction
```jsx
import { Accordion } from '@mantine/core';

function Demo() {
  return (
    <Accordion defaultValue="item-1">
      <Accordion.Item value="item-1">
        <Accordion.Control>Item 1</Accordion.Control>
        <Accordion.Panel>Content 1</Accordion.Panel>
      </Accordion.Item>
      <Accordion.Item value="item-2">
        <Accordion.Control>Item 2</Accordion.Control>
        <Accordion.Panel>Content 2</Accordion.Panel>
      </Accordion.Item>
    </Accordion>
  );
}
```

What happens:
1. Item 1 starts collapsed even though `defaultValue="item-1"` is set
2. Clicking on Item 1 control does nothing (or makes it collapse more?)
3. Clicking on Item 2 control shows Item 1's content instead
4. The whole behavior is inverted

### Expected behavior
- Item 1 should be expanded by default when `defaultValue="item-1"` is set
- Clicking an accordion control should expand/collapse the corresponding panel
- The panel visibility should match the active state

This seems like it started happening recently. Not sure if this is related to any recent changes but it's making the Accordion completely unusable in my app.

---
Repository: /testbed
