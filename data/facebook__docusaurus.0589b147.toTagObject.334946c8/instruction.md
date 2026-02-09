# Bug Report

### Describe the bug

When creating tags from front matter, the label and permalink values appear to be swapped. The tag label is being converted to kebab-case when it should preserve the original string, and the permalink is using the original string when it should be the kebab-cased version.

### Reproduction

```js
const tag = normalizeFrontMatterTag('/tags', 'My Tag Name');

console.log(tag.label); // Outputs: "my-tag-name" 
console.log(tag.permalink); // Outputs: "My Tag Name"

// Expected:
// tag.label should be: "My Tag Name"
// tag.permalink should be: "my-tag-name"
```

### Expected behavior

- The `label` field should contain the original tag string (e.g., "My Tag Name")
- The `permalink` field should contain the kebab-cased version (e.g., "my-tag-name")

Currently these values are reversed, which causes tags to display with incorrect formatting and generates invalid permalink URLs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
