# Bug Report

### Describe the bug

I'm experiencing an issue with data attribute handling in MDX. When using data attributes with hyphens (like `data-my-attribute`), the attribute name conversion to camelCase is incorrect, resulting in malformed property names.

### Reproduction

```js
// When processing an attribute like "data-my-value"
// Expected: dataMyValue
// Actual: data-MyValue (incorrect capitalization/format)

// Similarly, for attributes without hyphens like "datatest"
// Expected: dataTest  
// Actual: datast (missing character)
```

The conversion logic seems to be slicing the string at the wrong positions, causing either extra characters to be included or important characters to be dropped.

### Expected behavior

Data attributes should be properly converted to their camelCase equivalents:
- `data-my-attribute` → `dataMyAttribute`
- `datatest` → `dataTest`

The current behavior produces incorrect property names that don't match the expected camelCase format.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
