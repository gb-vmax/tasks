# Bug Report

### Describe the bug

I'm encountering an issue with directive containers in markdown parsing. When a directive container is immediately followed by a null character (end of input), the parser doesn't handle it correctly and the content doesn't get processed as expected.

### Reproduction

```js
const markdown = `
:::note
Some content here
:::
`

// Parse the markdown with directive containers
// The directive container content is not being entered/processed correctly
// when there's a null character after the opening
```

### Expected behavior

The parser should properly handle directive containers even when immediately followed by end of input. The `directiveContainerContent` should be entered and processed correctly regardless of what follows the container opening.

### Additional context

This seems to affect the flow of the tokenizer - the logic for determining when to enter the container content appears inverted. When there's actual content (non-null), it's exiting early instead of processing the content.

---
Repository: /testbed
