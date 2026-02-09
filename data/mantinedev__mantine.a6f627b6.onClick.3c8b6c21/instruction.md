# Bug Report

### Describe the bug

I'm experiencing an issue with the `AccordionControl` component where the accordion item doesn't toggle open/closed when clicking on it. After clicking the control button, nothing happens - the accordion stays in its current state.

### Reproduction

```jsx
import { Accordion } from '@mantine/core';

function Demo() {
  return (
    <Accordion>
      <Accordion.Item value="item-1">
        <Accordion.Control onClick={(event) => {
          console.log('clicked');
          // do some custom logic here
        }}>
          Click me
        </Accordion.Control>
        <Accordion.Panel>Content here</Accordion.Panel>
      </Accordion.Item>
    </Accordion>
  );
}
```

When I click on the accordion control, the console log appears but the accordion doesn't expand/collapse. It seems like the custom `onClick` handler is preventing the default toggle behavior.

### Expected behavior

The accordion should toggle open/closed when clicking the control, even when a custom `onClick` handler is provided. The custom handler should be called AND the accordion should still toggle its state.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
