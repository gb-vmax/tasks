# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links with resources are not being tokenized correctly. The parser seems to be completing the resource token before actually consuming the opening parenthesis character.

### Reproduction

```markdown
[link text](https://example.com)
```

When parsing markdown links with URLs, the tokenizer appears to exit the resource and resourceMarker tokens prematurely, before the opening parenthesis is consumed. This causes the link to not be parsed properly.

### Expected behavior

The tokenizer should:
1. Enter the resource token
2. Enter the resourceMarker token  
3. Consume the opening parenthesis `(`
4. Exit the resourceMarker token
5. Continue processing the resource content

Instead, it seems to be exiting tokens before consuming the character, which breaks the parsing flow.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have broken basic markdown link syntax. Any links with resource URLs are affected.

---
Repository: /testbed
