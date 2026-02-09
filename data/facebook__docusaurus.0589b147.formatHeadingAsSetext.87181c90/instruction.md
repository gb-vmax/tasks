# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading formatting where setext-style headings (underlined with `=` or `-`) are being used in unexpected situations. It seems like the logic for determining when to use setext vs ATX style headings (with `#` symbols) is not working correctly.

### Reproduction

When converting markdown AST nodes back to markdown text, headings that should be formatted as ATX style (with `#`) are sometimes being rendered as setext style instead, even when they contain line breaks or are at deeper nesting levels.

For example:
- Headings with depth 3 (h3) are being formatted as setext when they shouldn't be
- Headings containing literal line breaks in their content are being formatted as setext instead of ATX

### Expected behavior

The formatter should:
1. Only use setext style for h1 and h2 headings (depth 1 and 2)
2. Avoid setext style for headings that contain line breaks or break elements in their content
3. Default to ATX style (`#`, `##`, `###`, etc.) for h3 and deeper headings

### System Info
- remark version: 15.0.1

---
Repository: /testbed
