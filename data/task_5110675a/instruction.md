You are a backup operator tasked with testing the restore process on your Linux system. In the directory <code>/home/user/restore_test</code>, there are several backup files with the extension <code>.bak</code> (for example, <code>file1.bak</code>, <code>file2.bak</code>, etc.). Your goal is to automate the "restore" task with a Makefile.

Please create a <code>Makefile</code> in <code>/home/user/restore_test</code> with the following specifications:

<ul>
<li>A Makefile target named <code>restore</code> that, when run, copies each <code>.bak</code> file to a new file with the same base name but with the extension replaced by <code>.restored</code> (e.g., <code>file1.bak</code> → <code>file1.restored</code>).</li>
<li>The <code>restore</code> target must echo (print) <b>exactly</b> one line to the console for each successful restore, using this format (including spaces and punctuation):
<pre>
Restored: &lt;original_file.bak&gt; → &lt;restored_file.restored&gt;
</pre>
For example: <code>Restored: file1.bak → file1.restored</code>
</li>
<li>After running <code>make restore</code> in <code>/home/user/restore_test</code>, the system must contain new <code>.restored</code> files for each <code>.bak</code> file, and the correct console output lines for each restore.
</li>
</ul>

You do not need to clean up or remove files afterwards. Ensure the console output format and file outputs match the specifications exactly, as these will be automatically checked.
