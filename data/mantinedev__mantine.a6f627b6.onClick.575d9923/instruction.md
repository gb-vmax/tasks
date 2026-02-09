# Bug Report

### Describe the bug

When using `AccordionControl` with a custom `onClick` handler, the accordion item no longer toggles open/closed. The accordion state doesn't change when clicking on the control, even though the custom onClick handler is being executed.

### Reproduction

```jsx
<Accordion>
  <Accordion.Item value="item-1">
    <Accordion.Control onClick={(e) => console.log('clicked')}>
      Item 1
    </Accordion.Control>
    <Accordion.Panel>Content</Accordion.Panel>
  </Accordion.Item>
</Accordion>
```

### Expected behavior

The accordion should toggle open/closed when clicking the control, AND the custom onClick handler should execute. Both behaviors should work together.

### System Info

- Mantine version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
