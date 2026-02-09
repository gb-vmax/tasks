# Bug Report

### Issue with output generation - missing content

I've noticed that when processing MDX files, the generated output is sometimes incomplete or missing parts of the content. It seems like certain code blocks or text segments are being dropped during the compilation process.

### Reproduction

When compiling an MDX file with multiple sections:

```js
const mdx = `
# Hello World

Some introductory text here.

## Section 2

More content in this section.

\`\`\`js
const example = 'code block';
\`\`\`

Final paragraph.
`;

// After compilation, some sections are missing from the output
```

### Expected behavior

All content from the source MDX should be present in the compiled output. Currently it appears that some text is being lost, particularly when there are multiple consecutive writes to the output.

### Additional context

This seems to have started recently. The output is valid but incomplete - it's like some of the content just disappears during processing. Has anyone else experienced this?

---
Repository: /testbed
