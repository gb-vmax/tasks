# Bug Report

### Describe the bug

I'm experiencing issues with emphasis/strong markdown parsing when using asterisks (`*` or `**`) in certain contexts. It seems like the parser is not correctly determining when emphasis markers should open or close, particularly when dealing with punctuation or special characters around the markers.

### Reproduction

```markdown
**test**. more text

*emphasis* followed by punctuation

text with **bold** in the middle
```

When parsing the above markdown, the emphasis and strong markers don't behave as expected. The opening and closing logic seems to be inconsistent, especially when there's punctuation or whitespace involved.

### Expected behavior

The parser should correctly identify which asterisks are opening markers and which are closing markers based on the surrounding characters. According to CommonMark spec, the classification should depend on what comes before and after the marker.

For example:
- `**test**` should be parsed as strong emphasis
- `*emphasis*` should be parsed as emphasis
- The presence of punctuation shouldn't break the parsing logic

### Additional context

This appears to be related to how the `classifyCharacter` function is being used to determine the context before and after attention markers. The logic for determining whether a marker can open or close seems off.

---
Repository: /testbed
