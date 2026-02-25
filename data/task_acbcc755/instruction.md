As a technical writer, you have a directory at <code>/home/user/docs_project/final_drafts/</code> containing three Markdown files: <code>chapter1.md</code>, <code>chapter2.md</code>, and <code>chapter3.md</code>. Your goal is to organize and archive these chapters for handover.

1. Create a new directory at <code>/home/user/docs_project/archive/</code>.
2. Simultaneously (in parallel), compress each Markdown file in <code>/home/user/docs_project/final_drafts/</code> using gzip, such that the resulting <code>.gz</code> files are named after their respective chapters (for example, <code>chapter1.md.gz</code>). Place the compressed files into <code>/home/user/docs_project/archive/</code>.
3. Once all three files are compressed and moved, create a single tar archive <strong>named precisely</strong> <code>project_chapters_backup.tar</code> containing all three <code>.gz</code> files inside <code>/home/user/docs_project/archive/</code>.
4. Extract the <code>project_chapters_backup.tar</code> archive into a new folder at <code>/home/user/docs_project/restored/</code>.
5. Verify extraction by listing all <code>.gz</code> files in <code>/home/user/docs_project/restored/</code> and outputting this sorted list into a plain text file named <code>/home/user/docs_project/extraction_log.txt</code>. Each filename should be on a new line, with no extra spaces or lines, and sorted in ascending order.
6. Ensure that the <code>extraction_log.txt</code> file can be used by the automated test to verify that all three <code>.gz</code> files were properly extracted from the archive.

Pay special attention to:
- Directory names and file names matching exactly as specified.
- The log file <code>extraction_log.txt</code> containing precisely the sorted names of the three extracted <code>.gz</code> files, one per line, with no trailing whitespace.
- Only the <code>.gz</code> files are to be included in the tar archive and in the log.
