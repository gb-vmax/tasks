# Bug Report

### Describe the bug

I'm experiencing an issue with the `<Translate>` component where whitespace handling seems broken. When I format my JSX code with line breaks and indentation around the translation text, the component doesn't work correctly anymore.

### Reproduction

```jsx
<Translate id="my-translation">
  Some text to translate
</Translate>
```

When the translation text is on a separate line with indentation (which is normal JSX formatting), the translation doesn't seem to be extracted or processed properly. However, if I put everything on one line it works:

```jsx
<Translate id="my-translation">Some text to translate</Translate>
```

### Expected behavior

The `<Translate>` component should handle whitespace and formatting gracefully. It shouldn't matter whether the text content is on the same line as the opening/closing tags or formatted with line breaks and indentation. The translation extraction should work the same in both cases.

### Additional context

This is really annoying because prettier and other formatters naturally want to break up the JSX into multiple lines, but that seems to break the translation system. I have to disable formatting for these specific lines which is not ideal.

---
Repository: /testbed
