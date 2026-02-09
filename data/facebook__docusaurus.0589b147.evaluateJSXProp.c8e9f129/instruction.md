# Bug Report

### Describe the bug

I'm encountering an issue with the `<Translate>` component where statically evaluable props are being rejected and dynamic values are being accepted instead. The validation logic appears to be inverted - it's now warning about valid static strings and accepting non-confident/non-string values.

### Reproduction

```jsx
// This should work but triggers a warning
<Translate id="my.translation.id" description="A simple description">
  Hello World
</Translate>

// This should warn but seems to be accepted
<Translate id={someVariable} description={computedValue}>
  Dynamic content
</Translate>
```

When using the `<Translate>` component with static string values for `id` and `description` props (which should be the correct usage), I'm getting warnings that these props should be statically evaluable. Meanwhile, dynamically constructed values that should be rejected seem to pass through without warnings.

### Expected behavior

The component should:
- Accept static string literals for `id` and `description` props without warnings
- Reject and warn about dynamically constructed values that can't be extracted for translation

### Additional context

This seems to have started recently. The warning message also appears to be malformed - it's missing parts of the text like "Example:" and has truncated content.

---
Repository: /testbed
