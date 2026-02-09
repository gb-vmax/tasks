# Bug Report

### Describe the bug
I'm encountering an issue with directive parsing where text directives are not being processed correctly. It seems like the parser configuration has an incorrect reference that's preventing proper handling of inline text directives.

### Reproduction
```js
// Using a text directive in markdown content
const markdown = `
This is a :textDirective[with content] in the middle of text.
`

// Parse the markdown with remark-directive
const result = parseMarkdown(markdown)

// The text directive is not being recognized or parsed correctly
```

When trying to use inline text directives (`:directiveName[content]`), they're not being handled properly. The parser seems to be looking for the wrong type identifier.

### Expected behavior
Text directives should be properly recognized and parsed when they appear inline within text content. The `canContainEols` configuration should correctly reference the text directive type so that multi-line content within text directives is handled appropriately.

### Additional context
This appears to affect the markdown-to-AST conversion process. Container directives with labels also seem to have issues with their exit handlers not being called correctly during parsing.

---
Repository: /testbed
