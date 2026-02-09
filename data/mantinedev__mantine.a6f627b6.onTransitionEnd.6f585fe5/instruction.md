# Bug Report

### Describe the bug

The Accordion component is showing the opposite behavior - panels are collapsing when they should be expanding and expanding when they should be collapsing. When I click on an accordion item to open it, the panel closes instead, and vice versa.

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

Steps to reproduce:
1. Create an Accordion with `defaultValue` set to open an item
2. The item that should be open is closed
3. Click on any accordion control
4. The panel collapses instead of expanding

### Expected behavior

- Items specified in `defaultValue` should be expanded by default
- Clicking on a closed accordion item should expand it
- Clicking on an open accordion item should collapse it

This is making the accordion completely unusable in my application. Also noticed that the aria attributes seem to be swapped - the `id` and `aria-labelledby` values appear to be reversed.

---
Repository: /testbed
