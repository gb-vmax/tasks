# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where whitespace handling after line endings in JSX tags appears to be broken. The parser seems to be checking for whitespace conditions after already consuming the line ending code, which doesn't make sense since the code has already been consumed at that point.

### Reproduction

```mdx
<Component
  prop="value"
>
  Content here
</Component>
```

When parsing JSX tags with line breaks and whitespace, the parser enters an inconsistent state. After consuming a line ending character, it's trying to check if that same character is a space or unicode whitespace, but the character has already been consumed so this check will always fail.

Additionally, when encountering regular whitespace (not a line ending), the parser is now just entering "esWhitespace" state but not actually calling the continuation function `esWhitespaceInside`, which breaks the whitespace processing flow.

### Expected behavior

The parser should correctly handle whitespace and line endings in JSX tags without getting into an inconsistent state. Whitespace after line endings should be processed properly, and the whitespace handling flow should continue as expected.

### System Info
- MDX version: 3.0.0
- Parser: micromark-extension-mdx-jsx

---
Repository: /testbed
