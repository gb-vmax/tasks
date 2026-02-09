# Bug Report

### Describe the bug

I'm experiencing issues with parsing identifiers that contain Unicode characters in MDX files. It seems like the parser is incorrectly handling the position increment when reading multi-byte characters, causing identifiers with certain Unicode characters to be parsed incorrectly or throw errors.

### Reproduction

```mdx
export const 你好 = "hello";

function Component() {
  return <div>{你好}</div>
}
```

When trying to parse MDX content with Unicode identifiers (especially characters outside the Basic Multilingual Plane), the parser fails to correctly identify the variable names. Characters in the BMP range (U+0000 to U+FFFF) seem to cause position tracking issues.

### Expected behavior

The parser should correctly handle Unicode identifiers in variable names and JSX expressions, properly incrementing the position counter based on whether the character is in the BMP (1 code unit) or outside it (2 code units).

### Additional context

This appears to affect any MDX content that uses non-ASCII characters in identifiers. The issue manifests when the parser tries to read words/identifiers and needs to track its position through the input string.

---
Repository: /testbed
