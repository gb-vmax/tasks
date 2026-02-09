# Bug Report

### Describe the bug

I'm experiencing an issue with the `<Translate>` component where whitespace-only JSX text nodes are not being filtered out correctly during translation extraction. This causes problems when the component has formatting whitespace between tags.

### Reproduction

```jsx
<Translate id="my-translation" description="A test translation">
  
  Some text content
  
</Translate>
```

When using the `<Translate>` component with newlines and indentation around the actual text content, the extraction process doesn't properly handle these whitespace-only text nodes. This makes the translation system less reliable when dealing with formatted JSX.

### Expected behavior

The translation extractor should filter out empty or whitespace-only JSX text nodes and only process the actual content. Formatting whitespace (newlines, indentation) around the translation text should be ignored to make the system more robust to JSX formatting variations.

### Additional context

This seems to affect cases where:
- There are newlines before/after the translated text
- Indentation is used for code readability
- Multiple children exist with some being just whitespace

The extraction should be resilient to these common JSX formatting patterns.

---
Repository: /testbed
