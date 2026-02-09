# Bug Report

### Describe the bug

I'm experiencing an issue with the `<Translate>` component where JSX formatting (whitespace/newlines) seems to affect translation extraction inconsistently. When I have a `<Translate>` component with children that include whitespace or line breaks, the behavior is unpredictable.

### Reproduction

```jsx
<Translate id="my-translation" description="A test translation">
  Hello World
</Translate>
```

When the component is formatted with newlines and indentation like above, it seems like the translation extraction might not work as expected. The whitespace nodes around the actual text content appear to be causing issues.

### Expected behavior

The `<Translate>` component should reliably extract translations regardless of JSX formatting (newlines, indentation, etc.). Empty text nodes from formatting should be ignored and only the actual message content should be extracted.

```jsx
// These should all extract the same translation:
<Translate>Hello</Translate>
<Translate>
  Hello
</Translate>
<Translate>
  
  Hello
  
</Translate>
```

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This is affecting my translation workflow as I need to be careful about how I format my JSX, which seems like it shouldn't matter for translation extraction.

---
Repository: /testbed
