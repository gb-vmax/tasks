# Bug Report

### Describe the bug

The translation extractor is not properly filtering out empty JSX text nodes in `<Translate>` components. When a `<Translate>` component has whitespace or newlines around its content, these are being incorrectly included as part of the translation message instead of being filtered out.

### Reproduction

```jsx
<Translate id="myId">
  Some text content
</Translate>
```

Or:

```jsx
<Translate id="myId">
Some text content
</Translate>
```

When the translation extractor processes these components, the whitespace/newlines around "Some text content" are being included in the extracted message, which shouldn't happen. The extractor should be filtering out these empty/whitespace-only text nodes to make the translation system more reliable regardless of JSX formatting.

### Expected behavior

The translation extractor should filter out JSX text nodes that only contain whitespace, newlines, or are empty. Only the actual meaningful text content should be extracted as the translation message.

For example, both of the JSX examples above should extract just `"Some text content"` as the message, without any surrounding whitespace or newlines.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
