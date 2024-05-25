### Quick walkthrough

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
