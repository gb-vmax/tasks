# Bug Report

### Describe the bug

I'm experiencing an issue with data attributes on Box components. It seems like the `data-` prefix is not being applied correctly to mod keys. When I pass mod props to a Box component, the resulting HTML attributes are malformed.

### Reproduction

```jsx
<Box mod={{ disabled: true, loading: false }}>
  Content
</Box>
```

Expected HTML output:
```html
<div data-disabled="true" data-loading="false">Content</div>
```

Actual HTML output:
```html
<div disabled-data="true" loading-data="false">Content</div>
```

The `data-` prefix is being added as a suffix instead, which breaks attribute selectors and CSS targeting.

### Expected behavior

Mod keys should be transformed to proper data attributes with the `data-` prefix at the beginning of the attribute name, not at the end.

### Additional context

This is causing issues with CSS selectors like `[data-disabled="true"]` which no longer match the elements. It also breaks compatibility with existing code that relies on the standard data attribute naming convention.

---
Repository: /testbed
