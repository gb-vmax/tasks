# Bug Report

### Describe the bug

I'm encountering an issue with MDX processing where text nodes following break elements are being incorrectly spread into the parent array instead of being added as single elements. This causes the resulting AST structure to be malformed.

### Reproduction

```js
// When processing MDX content with breaks followed by text
const mdxContent = `
Some text
<br />
More text here
`;

// The text node after the break gets spread incorrectly
// Expected: values array contains proper node objects
// Actual: node properties get spread as individual array elements
```

### Expected behavior

When processing nodes after break elements, text nodes should be pushed to the values array as complete objects, not spread. The AST should maintain proper node structure with each element being a valid node object.

### Additional context

This appears to affect how content is rendered after line breaks in MDX documents. The logic for handling nodes that follow break elements seems to have the array spreading condition inverted - it's spreading non-array results and pushing array results directly, which is backwards from what it should be doing.

---
Repository: /testbed
