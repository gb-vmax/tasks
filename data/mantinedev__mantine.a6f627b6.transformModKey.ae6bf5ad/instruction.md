# Bug Report

### Describe the bug

When passing data attributes to components, the `data-` prefix is no longer being applied correctly. Custom mod attributes that should be transformed to data attributes are now being passed through without the prefix, breaking the expected behavior.

### Reproduction

```jsx
<Box mod={{ customProp: 'value' }}>
  Content
</Box>
```

Expected output in DOM:
```html
<div data-customProp="value">Content</div>
```

Actual output:
```html
<div customProp="value">Content</div>
```

The component is not adding the `data-` prefix to mod properties anymore. This affects any component using the Box component's mod system.

### Expected behavior

Mod properties should be automatically prefixed with `data-` when they don't already have it, so they become valid data attributes in the rendered HTML.

### Additional context

This seems to affect all components that use the Box mod system. The data attributes are important for styling and targeting elements with CSS selectors like `[data-customProp="value"]`.

---
Repository: /testbed
