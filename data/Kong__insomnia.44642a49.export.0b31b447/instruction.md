# Bug Report

### Describe the bug

The Nunjucks templating system is behaving incorrectly - it appears to be enabled when it should be disabled and vice versa. When I explicitly disable Nunjucks rendering via the `disable` prop, templates are still being processed. Conversely, when Nunjucks should be enabled (default behavior), it's not rendering templates at all.

### Reproduction

```jsx
// Case 1: Trying to disable Nunjucks
<NunjucksEnabledProvider disable={true}>
  {/* Templates are still being rendered here when they shouldn't be */}
  <RequestEditor />
</NunjucksEnabledProvider>

// Case 2: Default behavior (should be enabled)
<NunjucksEnabledProvider disable={false}>
  {/* Templates are NOT being rendered here when they should be */}
  <RequestEditor />
</NunjucksEnabledProvider>
```

### Expected behavior

When `disable={true}` is passed to `NunjucksEnabledProvider`, Nunjucks template rendering should be disabled and raw template strings should be visible/used. When `disable={false}` or no prop is passed, Nunjucks should be enabled and templates should be processed normally.

### System Info

- Insomnia version: latest
- OS: macOS

This seems like it started happening recently. The behavior is completely inverted from what it should be.

---
Repository: /testbed
