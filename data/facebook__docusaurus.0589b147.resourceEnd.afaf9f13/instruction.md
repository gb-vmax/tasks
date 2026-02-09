# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where the resource marker isn't being properly closed. When parsing markdown links with resources (like `[text](url "title")`), the parser seems to be handling the closing parenthesis incorrectly, which causes the resource node to not exit properly in the syntax tree.

### Reproduction

```js
// Parse a markdown link with a resource
const markdown = '[example](https://example.com "Example Title")';
const tree = processor.parse(markdown);

// The resource node structure is incomplete
// The "resource" exit event is missing from the token stream
```

### Expected behavior

When parsing markdown links with resources, the parser should properly enter and exit the "resource" node in the syntax tree. The closing parenthesis should trigger both the exit of "resourceMarker" and the exit of "resource" before returning.

### Additional context

This affects any markdown content with links that have resources (URLs with optional titles). The syntax tree structure becomes malformed which can cause issues with downstream processing or transformations.

---
Repository: /testbed
