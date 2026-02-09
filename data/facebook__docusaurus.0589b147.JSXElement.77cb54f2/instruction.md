# Bug Report

### Describe the bug

The translation extraction is failing for `<Translate>` components that have children with whitespace or formatting. After a recent update, components that were previously working are no longer being extracted properly.

### Reproduction

```jsx
<Translate id="my.translation" description="A sample translation">
  Hello World
</Translate>
```

When the component has formatting like this (which is common in JSX):

```jsx
<Translate 
  id="my.translation" 
  description="A sample translation"
>
  Hello World
</Translate>
```

The translation extraction seems to break or behave unexpectedly. The issue appears to be related to how whitespace and text nodes are being filtered/processed.

### Expected behavior

The translation extractor should handle `<Translate>` components consistently regardless of JSX formatting or whitespace. Both examples above should extract the same translation message.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues in our documentation build where previously working translations are no longer being extracted correctly.

---
Repository: /testbed
