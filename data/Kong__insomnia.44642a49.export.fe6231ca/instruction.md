# Bug Report

### Describe the bug

The `NunjucksEnabledProvider` component is not respecting the `disable` prop correctly. When I pass `disable={true}`, Nunjucks templating is still enabled instead of being disabled. It seems like the logic for determining the enabled state is inverted or broken.

### Reproduction

```tsx
// This should disable Nunjucks but it remains enabled
<NunjucksEnabledProvider disable={true}>
  <MyComponent />
</NunjucksEnabledProvider>

// Inside MyComponent, checking the context:
const { enabled } = useNunjucksEnabled();
console.log(enabled); // Expected: false, Actual: true
```

### Expected behavior

When `disable={true}` is passed to the provider, the context value should have `enabled: false`, effectively disabling Nunjucks rendering for all child components. When `disable={false}` or no prop is passed, `enabled` should be `true`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
