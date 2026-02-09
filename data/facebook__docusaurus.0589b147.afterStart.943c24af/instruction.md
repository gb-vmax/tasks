# Bug Report

### Describe the bug

I'm encountering an issue with parsing directives that have empty labels. When a directive uses the `[]` syntax with no content between the brackets, the parser doesn't handle it correctly and the resulting AST structure is malformed.

### Reproduction

```js
// Input markdown with empty label directive
const input = ':directive[]'

// Parse the directive
const result = parse(input)

// The AST structure is incorrect - the label markers and type 
// are not properly nested/closed
```

### Expected behavior

Empty label directives like `:directive[]` should be parsed correctly with proper AST node structure. The opening and closing bracket markers should be properly handled even when there's no content between them.

### Additional context

This seems to affect the order of operations when entering/exiting AST nodes for the label type and markers. The parser should handle the empty case the same way it handles labels with content.

---
Repository: /testbed
