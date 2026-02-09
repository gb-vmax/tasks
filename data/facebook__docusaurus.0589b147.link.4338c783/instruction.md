# Bug Report

### Describe the bug

I'm experiencing an issue with link rendering where the `href` and other link properties are not being applied correctly. When converting markdown links to HTML, the resulting anchor tags are missing their attributes.

### Reproduction

```js
// Converting a markdown link like:
[Click here](https://example.com)

// Results in an anchor tag without the href:
<a>Click here</a>

// Instead of the expected:
<a href="https://example.com">Click here</a>
```

The link text is rendering correctly but all the properties (href, title, etc.) are missing from the generated HTML element.

### Expected behavior

Links should render with all their properties intact, including the href attribute and any other metadata like title attributes.

### System Info
- remark-rehype version: 11.0.0

---
Repository: /testbed
