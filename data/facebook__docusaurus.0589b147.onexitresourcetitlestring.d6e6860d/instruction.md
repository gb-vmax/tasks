# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link titles not being parsed correctly. When I create a link with a title attribute, the title seems to disappear or not get attached to the correct node in the AST.

### Reproduction

```js
const markdown = '[Example](https://example.com "This is a title")'

// Parse the markdown
const result = remark().parse(markdown)

// The title is missing or in the wrong place
console.log(result)
```

When I inspect the parsed output, the link title is either missing entirely or seems to be attached to the wrong part of the syntax tree. This is breaking my documentation generator that relies on link titles for accessibility purposes.

### Expected behavior

The link node should have a `title` property containing `"This is a title"` that corresponds to the title text in the markdown link syntax.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
