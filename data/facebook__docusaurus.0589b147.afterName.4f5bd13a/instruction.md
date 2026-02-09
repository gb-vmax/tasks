# Bug Report

### Describe the bug

I'm encountering an issue with inline directive syntax parsing in remark-directive. It appears that directives with colons (`:`) in their names are being handled incorrectly - they're either not being parsed at all or causing unexpected behavior.

### Reproduction

```js
const markdown = ':directive-name[label]{attributes}'

// Parse with remark-directive
const result = processor.parse(markdown)

// The directive is not recognized/parsed correctly
```

When I try to use inline directives that contain certain characters, particularly colons, the parser doesn't handle them as expected. The directive either gets rejected when it should be accepted, or vice versa.

### Expected behavior

Inline directives should be parsed correctly according to the directive syntax specification. The parser should properly handle character validation for directive names and allow/reject them based on the correct rules.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

Has anyone else run into this? It seems like the character validation logic might have gotten inverted somehow.

---
Repository: /testbed
