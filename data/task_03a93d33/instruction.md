You are a build engineer tasked with organizing build artifacts for version 4.2.1 of a project. In the directory <code>/home/user/build_output</code>, you will find various files generated from the build process, including different types of files such as <code>.log</code>, <code>.o</code>, <code>.tmp</code>, and <code>.tar.gz</code> files. Your specific goal is the following:

1. Locate all files ending with the <code>.o</code> extension anywhere under <code>/home/user/build_output</code> (including subdirectories).
2. For every <code>.o</code> file you find, move it to a new directory called <code>/home/user/build_output/obj_archive</code>. If subdirectories are needed in <code>obj_archive</code> to mirror the original structure, replicate them.
3. Create a summary file named <code>/home/user/build_output/obj_archive/move-log.txt</code>. Each line in this file should list:
    <ul>
      <li>The original full path of the <code>.o</code> file</li>
      <li>an arrow (<code>-></code>)</li>
      <li>the new full path to its location in <code>obj_archive</code></li>
    </ul>
    <br/>
    For example, a line should look like:<br/>
    <code>/home/user/build_output/foo/bar.o -> /home/user/build_output/obj_archive/foo/bar.o</code>
4. Ensure that only the <code>.o</code> files are moved, leaving all other files untouched.

Please ensure that the <code>move-log.txt</code> file lists each move operation in the format specified above, one operation per line.
