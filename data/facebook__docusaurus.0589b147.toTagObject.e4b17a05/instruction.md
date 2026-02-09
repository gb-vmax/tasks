# Bug Report

### Describe the bug

I'm experiencing an issue with tag normalization where the tag label is being converted to kebab-case instead of preserving the original string. This causes tags to display incorrectly in the UI.

### Reproduction

```js
const tag = normalizeFrontMatterTag(tagsPath, 'My Custom Tag');
console.log(tag.label); // Expected: 'My Custom Tag', Actual: 'my-custom-tag'
```

When I define a tag like "React Native" or "Machine Learning" in my frontmatter, the labels are being transformed to "react-native" and "machine-learning" instead of keeping the original capitalization and spacing.

### Expected behavior

The `label` property should preserve the original tag string as-is, while only the `permalink` should be converted to kebab-case for URL purposes.

For example:
- Input: `"React Native"`
- Expected label: `"React Native"`
- Expected permalink: `"react-native"`

Currently both the label and permalink are being kebab-cased, which makes the tags look incorrect when displayed on the site.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
