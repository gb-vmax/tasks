# Bug Report

### Describe the bug

I'm experiencing an infinite loop/stack overflow when using certain attributes in MDX components. The browser becomes unresponsive and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```jsx
// This causes the browser to hang
<Component customAttribute="value" />
```

When rendering MDX with custom attributes that aren't in the standard attributes list, the application enters an infinite loop and becomes unresponsive.

### Expected behavior

Custom attributes should be handled gracefully without causing infinite recursion. The component should render normally with the custom attribute applied.

### System Info
- MDX version: 3.0.0
- Browser: Chrome/Firefox (both affected)
- Node version: 18.x

This seems to have started happening recently, possibly after an update to the property-information handling code. The issue appears to be related to attribute name transformation/lookup.

---
Repository: /testbed
