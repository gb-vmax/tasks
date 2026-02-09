# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where newlines are being inserted incorrectly between elements. It seems like extra newline characters are appearing in the output where they shouldn't be.

### Reproduction

When rendering MDX content with multiple nodes, the newlines between elements are not being handled correctly. 

```jsx
// Example MDX content with multiple elements
<div>First</div>
<div>Second</div>
<div>Third</div>
```

The output now has an extra newline at the beginning or between elements that shouldn't be there.

### Expected behavior

Newlines should only be inserted between actual elements in the array, not at positions where there are no valid separators needed. The first element shouldn't have a preceding newline when it's not supposed to.

### Additional context

This appears to be related to how the wrapping logic handles the iteration over nodes and determines when to insert text nodes with newline values. The condition for adding newlines seems to be off.

---
Repository: /testbed
