# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where links with empty destinations are not being handled correctly. When I try to use a markdown link with just `()` and no URL, the behavior seems wrong.

### Reproduction

```markdown
[link text]()
```

When parsing this MDX content, the link doesn't get processed as expected. It seems like the parser is treating the empty parentheses incorrectly.

### Expected behavior

Links with empty destinations like `[text]()` should be parsed properly. The parser should recognize this as a valid (though empty) link destination and handle it accordingly.

### Additional context

This appears to be related to how the tokenizer handles the resource part of links. The issue occurs specifically when there's no URL between the parentheses.

---
Repository: /testbed
