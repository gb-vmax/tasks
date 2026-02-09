# Bug Report

### Describe the bug

The `__getControlRef` callback is being called more times than expected in date picker components. I'm seeing an extra invocation beyond what should be happening based on the number of controls.

### Reproduction

```tsx
const Component = () => {
  const refCallback = (levelIndex, rowIndex, node) => {
    console.log('Control ref callback called', { levelIndex, rowIndex, node });
  };

  return (
    <DatePickerComponent
      __getControlRef={refCallback}
      // ... other props
    />
  );
};
```

When rendering the component, the callback is invoked one more time than the actual number of controls present. For example, if there are 42 controls, the callback gets called 43 times.

### Expected behavior

The `__getControlRef` callback should be called exactly once per control element, matching the `numberOfControls` value.

### Additional context

Also noticed that the callback is receiving different element types than expected - sometimes getting generic `HTMLElement` instead of the specific `HTMLButtonElement` type that the controls should be.

---
Repository: /testbed
