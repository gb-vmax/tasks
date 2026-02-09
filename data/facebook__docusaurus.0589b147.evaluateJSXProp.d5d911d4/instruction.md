# Bug Report

### Describe the bug

I'm experiencing an issue with the `<Translate>` component where the `id` and `description` props are not being extracted correctly. When I use string values for these props, they seem to be ignored or not processed as expected.

### Reproduction

```jsx
<Translate id="my.translation.id" description="This is a description">
  Hello World
</Translate>
```

When using the above code, the translation extraction doesn't work properly. The `id` and `description` values aren't being picked up during the build process.

### Expected behavior

The `id` and `description` props should be extracted from the `<Translate>` component so that translations can be properly generated. String literals passed to these props should be recognized and processed.

### System Info

- Docusaurus version: Latest
- Node version: 18.x

This seems to have started happening recently. Previously, the same code worked fine and translations were extracted without issues.

---
Repository: /testbed
