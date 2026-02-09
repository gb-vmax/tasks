# Bug Report

### Issue with MDX element properties being overwritten

I'm experiencing an issue where properties on MDX elements are being incorrectly overwritten when using custom data attributes. When I set properties on an element and also use `hProperties` in the data object, the original element properties get lost instead of being merged properly.

### Reproduction

```jsx
// MDX content with custom properties
export const meta = {
  hProperties: {
    className: 'custom-class',
    id: 'custom-id'
  }
}

<div className="original-class" data-test="value">
  Content here
</div>
```

The `hProperties` from the meta data completely replaces the original `className` and other properties on the div, rather than merging them together. I expected both the original properties and the hProperties to be present on the final element.

### Expected behavior

The properties should be merged so that both the original element properties and the `hProperties` are preserved. If there are conflicts, the hProperties should take precedence, but other properties should remain intact.

### Additional context

This seems to affect any element where properties are defined both inline and through the data object's hProperties. The original properties are getting wiped out completely.

---
Repository: /testbed
