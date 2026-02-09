# Bug Report

### Describe the bug

I'm experiencing an issue with identifier parsing in MDX content. It appears that certain valid identifier characters are being incorrectly processed, causing the parser to fail or behave unexpectedly when encountering specific character codes.

### Reproduction

When parsing MDX content that contains identifiers with certain characters (particularly those with character codes around or above 92), the tokenizer doesn't handle them correctly. This affects variable names and other identifiers in JSX expressions.

Example MDX content that triggers the issue:
```mdx
export const test = "value";

<Component prop={test} />
```

The parser seems to be treating some valid identifier characters differently than expected, leading to incorrect tokenization.

### Expected behavior

The parser should correctly identify and tokenize all valid JavaScript identifiers according to the ECMAScript specification, regardless of the character codes used in the identifier names. All valid identifier characters should be processed through the appropriate code path.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently and is blocking our ability to parse certain MDX files. Any help would be appreciated!

---
Repository: /testbed
