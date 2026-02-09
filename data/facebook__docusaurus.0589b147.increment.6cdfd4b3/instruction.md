# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute serialization where space-separated and comma-separated attributes are not being handled correctly. It seems like the bitmask values used internally for attribute types are producing unexpected results.

### Reproduction

When processing HTML with attributes that should be space-separated (like `class`) or comma-separated (like `accept`), the attribute serialization doesn't work as expected. The values appear to be getting mangled or not properly separated.

Example:
```js
const tree = {
  type: 'element',
  tagName: 'div',
  properties: {
    className: ['foo', 'bar', 'baz']
  }
}

// Expected: <div class="foo bar baz"></div>
// Getting incorrect output
```

Similar issues occur with comma-separated attributes like `accept` on input elements.

### Expected behavior

Attributes should be properly serialized with the correct separators:
- Space-separated attributes (like `class`) should join values with spaces
- Comma-separated attributes (like `accept`) should join values with commas
- Mixed attributes should handle both cases appropriately

### Additional context

This appears to affect the internal property information system that determines how different HTML attributes should be serialized. The issue manifests when rendering elements with multiple values for these attribute types.

---
Repository: /testbed
