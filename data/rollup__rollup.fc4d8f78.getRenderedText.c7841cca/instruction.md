# Bug Report

### Describe the bug

JSX text content is not being rendered correctly. It looks like whitespace handling is broken - text that should appear in the output is being stripped out entirely.

### Reproduction

```jsx
const Component = () => {
  return <div>  Some text with spaces  </div>
}
```

When this component renders, the text content appears to be empty or missing instead of displaying "Some text with spaces" with normalized whitespace.

### Expected behavior

JSX text nodes should have their whitespace normalized (multiple spaces collapsed to single spaces, leading/trailing whitespace trimmed) and the resulting text should be rendered. Text content should not disappear completely.

### Additional context

This seems to affect any JSX element with text content that has whitespace. The text either doesn't render at all or renders incorrectly. This is a pretty critical issue as it breaks basic text rendering in JSX.

---
Repository: /testbed
