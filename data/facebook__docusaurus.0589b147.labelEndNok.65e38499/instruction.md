# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links with nested brackets are not being handled correctly. It seems like the parser is accepting malformed link syntax that should be rejected.

### Reproduction

```js
const markdown = `[link [with nested] brackets](url)`;
const result = parse(markdown);

// The parser accepts this as valid when it should reject it
// Links with unbalanced brackets should not be parsed as valid links
```

When I try to parse markdown containing links with nested square brackets, the parser incorrectly treats them as valid links instead of rejecting them as malformed syntax.

### Expected behavior

Links with nested/unbalanced square brackets should be treated as invalid and not parsed as link elements. The parser should reject malformed link syntax like `[text [nested] text](url)`.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
