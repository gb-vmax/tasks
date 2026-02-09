# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown link titles that use single or double quotes. When I try to parse a link with a quoted title, the parser seems to incorrectly handle the title markers, causing the link to not be recognized properly.

### Reproduction

```js
// This should parse correctly but doesn't
const markdown = '[link](url "title")';
const result = parse(markdown);

// Also fails with single quotes
const markdown2 = "[link](url 'title')";
const result2 = parse(markdown2);
```

The links with quoted titles are not being parsed as expected. It seems like the parser is having trouble with the opening and closing quote markers.

### Expected behavior

Links with quoted titles (both single and double quotes) should be parsed correctly and the title should be extracted properly. The markdown spec allows for titles enclosed in quotes, so this should work.

### System Info
- Version: 15.0.1
- Node: 18.x

---
Repository: /testbed
