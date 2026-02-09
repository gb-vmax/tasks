# Bug Report

### Describe the bug

I'm encountering an issue with character entity parsing in MDX content. When using certain Unicode characters or character references in MDX files, they're being decoded incorrectly, resulting in garbled or unexpected output.

### Reproduction

```js
const mdxContent = `
# Test Document

Some text with character reference &#x1F600; (emoji)
And another one &#128512; (decimal reference)
`;

// Parse the MDX content
const result = parseMDX(mdxContent);

// The character references are not being decoded properly
console.log(result);
```

### Expected behavior

Character references (both hex and decimal) should be properly decoded to their corresponding Unicode characters. Emojis and other characters outside the basic multilingual plane should render correctly.

### Additional context

This seems to affect characters with code points above 65535 (characters that require surrogate pairs in UTF-16). The output shows incorrect characters instead of the expected emoji or special character.

Not sure if this is related to recent changes in the entity parsing logic, but it's definitely breaking content that was working before.

---
Repository: /testbed
