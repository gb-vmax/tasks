# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where links with resources are not being processed correctly. It seems like the parser is getting confused when trying to parse inline links with URLs and optional titles.

### Reproduction

```js
const markdown = '[link](https://example.com "title")'

// Parser throws an error or produces incorrect output
const result = remark().parse(markdown)
```

When trying to parse markdown links that include a URL and title in the resource notation `[text](url "title")`, the parser fails to handle them properly. The issue appears to be related to how the closing parenthesis is being processed.

### Expected behavior

The parser should correctly handle inline links with resources (URLs and optional titles) and produce the appropriate AST nodes without errors. Links like `[example](https://example.com "optional title")` should be parsed successfully.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken recently, as this syntax worked fine before. Any help would be appreciated!

---
Repository: /testbed
