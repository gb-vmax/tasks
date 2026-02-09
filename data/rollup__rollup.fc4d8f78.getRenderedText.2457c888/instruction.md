# Bug Report

### Describe the bug

JSX text content is not rendering correctly when it contains whitespace. The whitespace handling appears to be broken - spaces that should be preserved are being removed, and the output doesn't match what's expected.

### Reproduction

```jsx
const element = <div>
  Hello   World
</div>
```

When this JSX is processed, the whitespace between "Hello" and "World" is not handled properly. The text content gets mangled during the rendering process.

### Expected behavior

JSX text should properly normalize whitespace - collapsing multiple spaces into one and trimming leading/trailing whitespace, similar to how browsers handle HTML text content. The final rendered text should be `"Hello World"` with a single space between the words.

### Additional context

This seems to affect any JSX text nodes that contain multiple consecutive spaces or newlines with indentation. The whitespace normalization logic doesn't appear to be working as intended.

---
Repository: /testbed
