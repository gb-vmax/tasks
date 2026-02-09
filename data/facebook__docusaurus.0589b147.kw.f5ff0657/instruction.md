# Bug Report

### Describe the bug

I'm experiencing an issue where keyword token types are not being created with the correct options. It seems like the `keyword` property is being added to the options object after the TokenType is instantiated, which means the TokenType constructor doesn't receive the keyword information.

### Reproduction

```js
// When creating a keyword token type
const keywordToken = kw('const', { beforeExpr: true });

// The keyword property should be passed to TokenType constructor
// but it's being set on options AFTER TokenType is created
```

The problem is that the `options.keyword` assignment happens after the `new TokenType()` call, so the TokenType instance is created without knowing it's a keyword token.

### Expected behavior

The keyword property should be included in the options when the TokenType is instantiated, so that the TokenType constructor receives all the necessary information including the keyword designation.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
