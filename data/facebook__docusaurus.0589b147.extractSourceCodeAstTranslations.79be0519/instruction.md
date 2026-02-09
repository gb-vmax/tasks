# Bug Report

### Describe the bug

I'm experiencing an issue with the translation extraction where components with whitespace-only text nodes are being incorrectly filtered out. When I have a `<Translate>` component with actual content that includes newlines or spaces, the content is not being extracted properly.

### Reproduction

```jsx
<Translate id="my.translation">
  Some text with newlines
</Translate>
```

The translation extractor seems to be skipping this content even though it's not empty. It looks like the logic for filtering out empty/whitespace nodes might be inverted.

### Expected behavior

The extractor should correctly identify and extract non-empty text content from `<Translate>` components, even when the text contains newlines or other whitespace characters. Only truly empty text nodes (those that are just whitespace) should be filtered out.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
