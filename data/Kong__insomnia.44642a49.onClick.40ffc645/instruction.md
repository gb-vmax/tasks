# Bug Report

### Describe the bug

The `AsyncButton` component is broken after a recent change. When I click the button, the `onClick` handler is not being called at all. The button appears to do nothing.

### Reproduction

```tsx
<AsyncButton
  onClick={async (event) => {
    console.log('Button clicked');
    await someAsyncOperation();
  }}
>
  Click Me
</AsyncButton>
```

When clicking the button, nothing happens - no console log, no async operation is executed.

### Expected behavior

The `onClick` handler should be invoked when the button is clicked, and any async operations should be awaited properly.

### Additional context

This was working fine before, but now the button is completely unresponsive. It looks like the component interface might have been modified incorrectly - there seems to be a function definition where a property type should be.

---
Repository: /testbed
