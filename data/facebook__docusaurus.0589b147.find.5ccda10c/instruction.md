# Bug Report

### Describe the bug

I'm experiencing an issue with data attribute handling in MDX. When using data attributes with dashes (like `data-test-id`), the attribute names are being transformed incorrectly, causing them to not work as expected.

### Reproduction

```jsx
// Using a data attribute with a dash
<div data-test-id="my-component">
  Content
</div>
```

When this gets processed, the data attribute isn't being handled correctly. It seems like the transformation logic for converting kebab-case data attributes to camelCase is broken.

### Expected behavior

Data attributes like `data-test-id` should be properly normalized and accessible. The dash-separated format should be correctly converted to the appropriate JavaScript property name.

### Additional context

This appears to affect data attributes that:
1. Start with `data-` followed by a dash (e.g., `data-test-id`, `data-custom-value`)
2. Start with `data` followed directly by a capital letter or lowercase letter

The attribute name transformation seems to be producing incorrect results, causing the attributes to either be malformed or not recognized properly.

---
Repository: /testbed
