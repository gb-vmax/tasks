# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where operator tokens are being extracted incorrectly. It appears that operators are missing their first character when being parsed.

### Reproduction

When parsing MDX content that contains operators, the parser seems to skip the first character of the operator token. For example:

```js
// Input MDX with operators like ===, !==, +=, etc.
const mdxContent = `
export const value = 1 + 2;
if (x === y) { }
`;

// After parsing, operators are truncated
// Expected: "===" 
// Actual: "=="
```

This affects all operators including comparison operators (`===`, `!==`), compound assignment (`+=`, `-=`), and others. The operator is recognized but the extracted string is one character short.

### Expected behavior

Operators should be extracted with all their characters intact. A `===` operator should be tokenized as `"==="`, not `"=="`.

### System Info
- MDX version: 3.0.0
- Parser: acorn-based tokenizer

This seems to have started happening recently. Not sure if this is related to a recent change in the tokenization logic.

---
Repository: /testbed
