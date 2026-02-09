# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links with whitespace between the destination URL and the title are not being processed correctly. The parser seems to be handling the whitespace incorrectly, causing links to either fail to parse or produce unexpected output.

### Reproduction

```markdown
[link text](https://example.com "title text")
```

When parsing markdown with links that have whitespace between the URL and the title (which is valid markdown syntax), the output is incorrect or the link fails to be recognized.

This also affects links with line breaks:
```markdown
[link text](https://example.com
"title text")
```

### Expected behavior

Both of the above markdown examples should parse correctly and produce valid links with the URL and title properly separated. The parser should handle whitespace (including spaces and line endings) between the destination and title as per the CommonMark specification.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
