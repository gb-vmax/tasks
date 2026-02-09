# Bug Report

### Describe the bug

I'm encountering an issue with MDX rendering where nested arrays are not being flattened correctly in the output. When processing child elements, the resulting JSX structure contains nested arrays instead of a flat list of elements.

### Reproduction

```jsx
// MDX content with multiple child elements
<div>
  <span>First</span>
  <span>Second</span>
  <span>Third</span>
</div>
```

When this gets processed, the children array structure becomes:

```js
// Expected: [element1, element2, element3]
// Actual: [[element1, element2, element3]]
```

This causes rendering issues where the nested array structure breaks the component tree.

### Expected behavior

Child elements should be properly flattened into a single-level array. When `handle()` returns an array of results, those results should be spread into the parent results array, not pushed as a nested array.

### Additional context

This seems to affect any MDX content with multiple sibling elements. The issue appears to be in how child elements are being collected during the transformation process.

---
Repository: /testbed
