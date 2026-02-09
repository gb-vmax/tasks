# Bug Report

### Describe the bug

When passing a non-array `classNames` object to a component, the styles are not being applied correctly. The component renders without the expected class names.

### Reproduction

```jsx
const MyComponent = () => {
  return (
    <Button
      classNames={{
        root: 'custom-root',
        label: 'custom-label'
      }}
    >
      Click me
    </Button>
  );
};
```

### Expected behavior

The button should have the `custom-root` and `custom-label` classes applied to the respective elements. Previously this worked fine, but now the classes are missing from the rendered output.

### Additional context

This seems to have started happening recently. When I inspect the DOM, the custom class names are completely absent. If I pass `classNames` as an array it works, but passing a single object (which should be valid according to the docs) doesn't work anymore.

---
Repository: /testbed
