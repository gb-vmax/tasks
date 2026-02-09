# Bug Report

### Describe the bug

I'm encountering an issue with hard breaks in markdown rendering. When using hard breaks (two spaces at the end of a line), the position information seems to be incorrect, and line endings aren't being handled properly in certain contexts.

### Reproduction

```js
const markdown = `This is a line with hard break  
This is the next line`;

// Parse the markdown
const result = remark().parse(markdown);

// The position end point for hard breaks appears incorrect
// Also, line endings in certain container elements are not being processed as expected
```

### Expected behavior

- Hard breaks should have correct position information (end point should reflect the actual end of the token)
- Line endings should be properly handled based on whether the parent context can contain end-of-line elements

### Additional context

This seems to affect how the AST positions are calculated for hard breaks and how line endings are processed in different container contexts. The behavior changed recently and is causing issues with position tracking in my markdown processor.

---
Repository: /testbed
