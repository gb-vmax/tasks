# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag parsing where self-closing tags are being treated as if they're always self-closing, even when they shouldn't be. This causes problems when working with JSX components that have opening and closing tags.

### Reproduction

```jsx
// This component with opening and closing tags
<MyComponent>
  <p>Content here</p>
</MyComponent>

// Gets parsed incorrectly - the selfClosing flag seems to be set to true by default
// instead of false, which breaks the tag matching logic
```

When parsing MDX content with JSX components that have both opening and closing tags, the parser seems to initialize all tags as self-closing rather than determining this based on the actual syntax.

### Expected behavior

- Opening tags (like `<MyComponent>`) should have `selfClosing: false`
- Only actual self-closing tags (like `<MyComponent />`) should have `selfClosing: true`
- The parser should correctly match opening and closing tag pairs

### Additional context

This appears to be related to how the tag object is initialized when entering a JSX tag during parsing. The default value for the `selfClosing` property might be incorrect.

---
Repository: /testbed
