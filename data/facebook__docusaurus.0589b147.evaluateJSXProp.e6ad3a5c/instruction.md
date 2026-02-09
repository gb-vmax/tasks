# Bug Report

### Describe the bug

The `<Translate>` component is not extracting translation strings correctly. When I use the component with `id` and `description` props, the translation extraction seems to be completely broken and the props are not being recognized.

### Reproduction

```jsx
<Translate id="homepage.title" description="Title for the homepage">
  Welcome to my site
</Translate>
```

When running the translation extraction, the `id` and `description` props are not being picked up at all. It's like the component attributes are being ignored entirely.

I've also noticed that the warning messages that should appear when using dynamic values look corrupted/malformed.

### Expected behavior

The translation extractor should:
1. Correctly identify and extract the `id` prop value ("homepage.title")
2. Correctly identify and extract the `description` prop value ("Title for the homepage")
3. Extract the child text content ("Welcome to my site")
4. Show proper warning messages if dynamic values are used

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like a regression as it was working fine before. Any help would be appreciated!

---
Repository: /testbed
