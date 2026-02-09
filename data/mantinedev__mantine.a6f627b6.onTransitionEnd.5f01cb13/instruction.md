# Bug Report

### Accordion panels showing/hiding in reverse

I'm experiencing an issue with the Accordion component where panels are behaving in the opposite way they should. When I click on an accordion item to expand it, the panel collapses instead, and when I click to collapse it, it expands.

### Reproduction

```jsx
import { Accordion } from '@mantine/core';

function Demo() {
  return (
    <Accordion defaultValue="item-1">
      <Accordion.Item value="item-1">
        <Accordion.Control>Item 1</Accordion.Control>
        <Accordion.Panel>
          Content for item 1
        </Accordion.Panel>
      </Accordion.Item>
      <Accordion.Item value="item-2">
        <Accordion.Control>Item 2</Accordion.Control>
        <Accordion.Panel>
          Content for item 2
        </Accordion.Panel>
      </Accordion.Item>
    </Accordion>
  );
}
```

### Expected behavior

- Item 1 should be expanded by default (since `defaultValue="item-1"`)
- Clicking on Item 1's control should collapse it
- Clicking on Item 2's control should expand it

### Actual behavior

- Item 1 is collapsed by default even though `defaultValue="item-1"` is set
- Clicking on Item 1's control expands it (should collapse)
- Clicking on Item 2's control does nothing or shows unexpected behavior

The accordion seems to be working in reverse - closed items appear open and open items appear closed. This makes the component unusable in its current state.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
