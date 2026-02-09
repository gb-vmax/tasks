# Bug Report

### Describe the bug

I'm experiencing an issue with the `<Translate>` component where JSX whitespace and formatting seems to affect translation extraction. When I have a `<Translate>` component with children that include JSX text nodes, the extraction behavior appears inconsistent.

### Reproduction

```jsx
<Translate id="my-translation" description="A sample translation">
  Some text content here
</Translate>
```

When using the Translate component with whitespace or formatting around the text content, the translation extraction doesn't work as expected. It seems like empty or whitespace-only JSX text nodes might be interfering with how the content is processed.

### Expected behavior

The translation extractor should properly handle JSX formatting and whitespace, filtering out empty/insignificant text nodes and extracting the actual translation message consistently regardless of how the JSX is formatted.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
