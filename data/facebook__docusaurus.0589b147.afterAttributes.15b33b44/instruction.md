# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the parser seems to be failing when processing attributes in container directives. After some investigation, it appears that whitespace handling after directive attributes is not working as expected.

### Reproduction

```js
const input = `
:::note{#id}
Content here
:::
`;

// Parser fails to correctly process the directive
const result = parse(input);
```

The parser doesn't seem to handle the whitespace correctly after the attribute block `{#id}`, causing the directive container to not be recognized or parsed properly.

### Expected behavior

The directive container should be parsed correctly regardless of whitespace after attributes. The parser should properly handle the transition from attributes to the content block.

### Additional context

This seems to affect any container directive that has attributes followed by content. Simple directives without attributes work fine, but once you add attributes like `{#id}` or `{.class}`, the parsing breaks down.

---
Repository: /testbed
