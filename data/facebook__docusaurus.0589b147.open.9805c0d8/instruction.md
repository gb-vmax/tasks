# Bug Report

### Describe the bug
HTML closing tags are not being parsed correctly in markdown content. When I try to use closing tags like `</div>` or `</span>` in my markdown files, they're not being recognized and the HTML structure gets broken.

### Reproduction
```markdown
<div>
  <p>Some content here</p>
</div>
```

When parsing this markdown, the closing `</div>` tag is not being handled properly. It seems like the parser is treating the `/` character incorrectly and not recognizing it as the start of a closing tag.

### Expected behavior
The parser should correctly identify and process HTML closing tags (tags starting with `</`) in markdown content. The opening and closing tags should match up properly.

### Additional context
This appears to affect all HTML closing tags in markdown. Regular opening tags and self-closing tags seem to work fine, but anything with `</` is broken.

---
Repository: /testbed
