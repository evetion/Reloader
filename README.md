# <img src=layer-reload.png width="30"> QGIS Reloader 
Reload selected layer(s).

Simple utility to reload/reopen selected layer(s). Reloading updates the data,
reopen also updates the extent. Also provides an option to watch layer
for changes to local file paths and reloads them automatically.
Useful when you're editing the underlying data on the fly in some other program.

In addition to e.g. shapefiles, delimited text files can also be monitored.  To 
do this open the `Properties` for the layer that is joined to the delimited file 
(not the delimited file's layer) and select that file's layer in the list under 
`Dependencies`, then under `Joins` edit the join layer and make sure `Cache join 
layer in memory` is not selected.  After doing this the joined layer should 
update automatically when the watched delimited text file changes.

![](screenshot.png)
