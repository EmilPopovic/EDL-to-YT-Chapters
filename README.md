# Quick walkthrough

This is a simple scirpt made to convert DaVinci Resolve timeline markers exported to EDL to a YouTube chapters/timestamps friendly format. This script may or may not work for exports from other editing softwares.

To export the EDL right click on your timeline in the Media Pool (Edit page) and follow the next picture:

![image](https://github.com/EmilPopovic/EDL-to-YT-Chapters/assets/104315710/e57d977b-3539-436b-a6e2-5264e59760d3)

The exported file (input for this script) will look something like this:

```
TITLE: timestamp file name
FCM: NON-DROP FRAME

001  001      V     C        01:00:00:00 01:00:00:01 01:00:00:00 01:00:00:01  
 |C:ResolveColorBlue |M:The first marker name |D:1

002  001      V     C        01:20:09:21 01:20:09:22 01:20:09:21 01:20:09:22  
 |C:ResolveColorBlue |M:Name of the second marker |D:1

003  001      V     C        02:04:42:05 02:04:42:06 02:04:42:05 02:04:42:06  
 |C:ResolveColorBlue |M:And there is a third one? |D:1

...
```

The output file will look like:

```
0:00 The first marker name
20:09 Name of the second marker
1:04:42 And there is a third one?
```

# Using the GUI

To use the GUI, start app.py or the packaged version.

You will see something similar to this:

![image](https://github.com/user-attachments/assets/b902d571-f043-4686-b196-7c48f805ee4d)

After dragging and dropping or selecting the file, its path will be shown. You can deselect it or select another one right away.

![image](https://github.com/user-attachments/assets/03d038f2-64fd-4d6f-b961-6863c1f615b1)

It is possible to preview the file and copy the exported timestamps without saving it to a text file, though that is an option too.

![image](https://github.com/user-attachments/assets/9c272ea5-e2d7-4de0-8629-9a9ef6660427)


# Using the CLI script

To use from terminal, simply start edl_to_yt.py.

When starting, the script will ask you for the input and output file paths:

```
Enter path to .edl file > ...
Enter output path > ...
```

If any errors are encountered, an exception will be thrown. If no errors occur, `SUCCESS` will be printed to the console.

Conditions that throw errors:
- input path is not an EDL file
- the first timestamp is not 0:00 (required by YouTube)
- not all timestamps are at least 10 seconds apart (required by YouTube)
