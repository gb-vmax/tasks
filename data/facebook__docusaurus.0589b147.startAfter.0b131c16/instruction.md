# Bug Report

### Describe the bug

I'm experiencing an issue with MDX tag parsing where tags followed by whitespace are being rejected incorrectly. It seems like the parser is not properly handling cases where there's whitespace after the opening tag marker.

### Reproduction

```mdx
<Component >
  content
</Component>
```

or

```mdx
<div 
  className="test"
>
  content
</div>
```

### Expected behavior

Tags with whitespace after the opening `<` should be parsed correctly. This is valid JSX/HTML syntax and should work in MDX files.

### Current behavior

The parser appears to reject these tags and fails to process them properly. The whitespace after the tag marker seems to be causing the parser to incorrectly identify these as invalid syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a regression as this syntax worked in previous versions. Any help would be appreciated!

---
Repository: /testbed
