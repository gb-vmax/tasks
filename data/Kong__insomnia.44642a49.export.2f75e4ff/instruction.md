# Bug Report

### Describe the bug

After a recent update, the `NunjucksEnabledProvider` context is not working as expected when nested. The enabled state seems to be ignoring the parent context values, causing child components to have incorrect Nunjucks rendering behavior.

### Reproduction

```jsx
<NunjucksEnabledProvider disable={false}>
  <ParentComponent>
    <NunjucksEnabledProvider disable={true}>
      <ChildComponent />
    </NunjucksEnabledProvider>
  </ParentComponent>
</NunjucksEnabledProvider>
```

When nesting `NunjucksEnabledProvider` components like above, the child provider doesn't seem to properly inherit or respect the parent's enabled state. The Nunjucks templating is either always enabled or always disabled regardless of the parent context.

### Expected behavior

The nested provider should inherit the parent context's enabled state when not explicitly overridden. If a parent has `disable={true}`, nested children should also be disabled unless explicitly enabled. The context should properly cascade through the component tree.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking our nested request/response rendering where we need to conditionally enable/disable Nunjucks templating at different levels of the component hierarchy.

---
Repository: /testbed
