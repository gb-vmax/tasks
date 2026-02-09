# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where image links (`![alt](url)`) are not being processed correctly. It seems like the parser is treating image links the same way as regular links, which causes incorrect offset calculations during parsing.

### Reproduction

```markdown
![image](https://example.com/image.png)
[link](https://example.com/page)
```

When parsing the above markdown:
- Image links are not being recognized properly
- The offset calculation appears to be wrong for image syntax
- Regular links might also be affected in certain nested scenarios

### Expected behavior

The parser should correctly distinguish between image links (`![...]`) and regular links (`[...]`), applying the appropriate offset (2 for images vs 0 for regular links) during the label resolution phase.

### Additional context

This affects markdown documents that contain image links. The issue seems to be in the label end resolution logic where the parser determines whether it's dealing with an image or a regular link.

---
Repository: /testbed
