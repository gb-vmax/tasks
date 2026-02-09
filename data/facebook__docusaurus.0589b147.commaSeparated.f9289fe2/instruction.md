# Bug Report

### Describe the bug

I'm encountering an issue with comma-separated attribute values in MDX. When I have an array with a single item, it's being rendered with a trailing comma, and arrays with multiple items are missing the last element entirely.

### Reproduction

```js
// Single item array - outputs "item1," instead of "item1"
<Component data={['item1']} />

// Multiple items - outputs "item1, item2" instead of "item1, item2, item3"
<Component data={['item1', 'item2', 'item3']} />
```

The comma-separated serialization seems to be broken. Single-item arrays get an unexpected trailing comma, and multi-item arrays are truncated (the last item is completely missing from the output).

### Expected behavior

- Single item arrays should serialize without a trailing comma: `"item1"`
- Multiple item arrays should include ALL items: `"item1, item2, item3"`

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
