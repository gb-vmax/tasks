# Bug Report

### Describe the bug

I'm encountering an issue with the remark-mdx parser where it's failing to parse certain regular expression patterns correctly. It seems like the parser is no longer recognizing class set reserved punctuators in regex character classes, which is causing parsing errors for valid MDX content.

### Reproduction

When trying to parse MDX content that contains regex patterns with special punctuation characters in character classes, the parser throws an error or produces incorrect output.

For example, content like:

```mdx
export const pattern = /[&@#]/;
```

or

```mdx
const regex = /[!%,]/;
```

These patterns should be valid but are not being parsed correctly. The issue appears to be related to how the parser handles reserved punctuators within regex character class sets.

### Expected behavior

The parser should correctly handle regex patterns containing reserved punctuators like `&`, `@`, `#`, `!`, `%`, `,`, etc. within character classes. These are valid regex syntax and should parse without errors.

### Additional context

This seems to have broken after a recent update. The parser was working fine with these patterns before. It looks like something changed in how character class set syntax is being validated.

---
Repository: /testbed
