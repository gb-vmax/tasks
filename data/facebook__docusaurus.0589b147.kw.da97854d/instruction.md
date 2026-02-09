# Bug Report

### Describe the bug

I'm encountering an issue with keyword token types after a recent update. The `kw()` function appears to be returning the wrong value, which is breaking functionality that depends on getting the actual TokenType object back.

### Reproduction

```js
const keywordType = kw('const', { beforeExpr: true });

// keywordType should be a TokenType instance, but it's returning something else
console.log(keywordType); // Expected: TokenType { label: 'const', ... }
                          // Actual: { keyword: 'const', beforeExpr: true }
```

When creating keyword tokens, the function is supposed to return the TokenType instance that gets stored in the keywords object. However, it seems to be returning the options object instead.

### Expected behavior

The `kw()` function should return the TokenType instance that was created and stored in the keywords registry, not the options object that was passed in.

### System Info
- remark-mdx version: 3.0.0
- Node: v18.x

---
Repository: /testbed
