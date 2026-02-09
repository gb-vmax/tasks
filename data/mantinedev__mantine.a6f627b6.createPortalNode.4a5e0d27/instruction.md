# Bug Report

### Describe the bug

When passing `className` prop to Portal component, multiple CSS classes are not being applied correctly. Instead of adding each class separately to the classList, they're being joined and added as a single class name.

### Reproduction

```jsx
<Portal className="class-one class-two class-three">
  <div>Portal content</div>
</Portal>
```

When inspecting the portal node in the DOM, the classes are not applied as expected. The element should have three separate classes in its classList, but instead they appear to be combined incorrectly.

### Expected behavior

The portal node should have all classes from the `className` prop properly added to its classList, with each class name being a separate entry. For example, if `className="modal-overlay z-index-high"` is passed, both `modal-overlay` and `z-index-high` should be present as individual classes on the element.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
