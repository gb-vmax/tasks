# Bug Report

### Describe the bug

The `NunjucksEnabledProvider` component is not behaving correctly when the `disable` prop is passed. When I set `disable={true}`, Nunjucks templating is still being enabled instead of disabled. The logic seems inverted - passing `disable={true}` should disable Nunjucks, but it's doing the opposite.

### Reproduction

```jsx
// This should disable Nunjucks but it's still enabled
<NunjucksEnabledProvider disable={true}>
  <MyComponent />
</NunjucksEnabledProvider>

// Inside MyComponent, checking the context:
const { enabled } = useNunjucksEnabled();
console.log(enabled); // Expected: false, Actual: true
```

### Expected behavior

When `disable={true}` is passed to `NunjucksEnabledProvider`, the context value should have `enabled: false` and Nunjucks templating should be disabled. When `disable={false}` or no prop is passed, `enabled` should be `true`.

### Additional context

This is affecting template rendering in my requests where I need to conditionally disable Nunjucks processing. The inverted logic is causing templates to be processed when they shouldn't be.

---
Repository: /testbed
