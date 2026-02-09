# Bug Report

### Describe the bug

I'm experiencing an issue with HTML tag parsing in markdown content. When processing closing tags, alphanumeric characters are being incorrectly handled, which causes the parser to consume characters it shouldn't.

### Reproduction

```js
// Example markdown with HTML closing tag
const markdown = `
<div>
  content here
</div>
`

// When parsing, the closing tag </div> doesn't get recognized properly
// Alphanumeric characters in the tag name are being skipped instead of consumed
```

### Expected behavior

The parser should correctly identify and process closing HTML tags with alphanumeric characters in their names. The tag closing logic should consume alphanumeric characters as part of the tag name until it reaches a non-alphanumeric character.

### Additional context

This seems to affect any HTML closing tags in markdown content. The logic for determining which characters belong to the tag name appears to be inverted - it's treating alphanumeric characters as terminators rather than valid tag name characters.

---
Repository: /testbed
