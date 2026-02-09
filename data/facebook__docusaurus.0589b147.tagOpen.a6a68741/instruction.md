# Bug Report

### Describe the bug
I'm encountering an issue with HTML tag parsing in markdown content. When using certain HTML tags with hyphens in the tag name (like custom elements), they're not being recognized correctly anymore.

### Reproduction
```markdown
This is some text with <custom-element>content</custom-element> inline.
```

When processing this markdown, the HTML tag with a hyphen in its name doesn't get parsed properly. The tag is being treated as plain text instead of being recognized as an HTML element.

### Expected behavior
HTML tags containing hyphens (like custom elements or web components) should be parsed correctly as valid HTML tags, just like standard HTML tags without hyphens.

### Additional context
This seems to affect custom elements and any HTML tags that use hyphens in their names. Standard HTML tags like `<div>` and `<span>` still work fine.

---
Repository: /testbed
