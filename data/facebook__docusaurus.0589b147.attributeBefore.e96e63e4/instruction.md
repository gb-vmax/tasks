# Bug Report

### Describe the bug

I'm encountering an issue with self-closing JSX/MDX tags. When I try to use the standard self-closing syntax with a forward slash (`/>`), it's not being recognized properly. Instead, it seems like the parser is expecting a different character.

### Reproduction

```jsx
// This doesn't work as expected
<Component />

// Trying to use self-closing tags in MDX
<CustomElement attr="value" />
```

When I write JSX/MDX with self-closing tags using the normal `/` syntax, the parser doesn't handle them correctly. This is breaking all my self-closing components.

### Expected behavior

Self-closing tags with `/>` should be parsed correctly. This is standard JSX/MDX syntax and should work without issues.

```jsx
<Component />
<div className="test" />
<img src="test.jpg" />
```

All of these should be valid self-closing tags.

### Additional context

This seems to have started happening recently. The self-closing marker detection appears to be looking for the wrong character code. Standard JSX/MDX uses forward slash (`/`) for self-closing tags, but something in the parsing logic might have changed.

---
Repository: /testbed
