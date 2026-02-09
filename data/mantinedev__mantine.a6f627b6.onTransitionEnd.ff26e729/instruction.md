# Bug Report

### Describe the bug

The Accordion component is behaving in reverse - panels are now collapsing when they should be expanding and expanding when they should be collapsing. When I click on an accordion item to open it, the panel closes instead, and clicking a closed item opens it.

### Reproduction

```jsx
import { Accordion } from '@mantine/core';

function Demo() {
  return (
    <Accordion defaultValue="item-1">
      <Accordion.Item value="item-1">
        <Accordion.Control>Item 1</Accordion.Control>
        <Accordion.Panel>
          This panel should be visible by default but it's hidden
        </Accordion.Panel>
      </Accordion.Item>
      <Accordion.Item value="item-2">
        <Accordion.Control>Item 2</Accordion.Control>
        <Accordion.Panel>
          This panel should be hidden but appears visible
        </Accordion.Panel>
      </Accordion.Item>
    </Accordion>
  );
}
```

### Expected behavior

- When an accordion item is active/selected, its panel should be visible (expanded)
- When an accordion item is inactive, its panel should be hidden (collapsed)
- The `defaultValue` prop should show the corresponding panel on initial render

### Current behavior

The opposite happens - active items show collapsed panels and inactive items show expanded panels.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
