# <img src=layer-reload.png width="30"> QGIS Reloader 
Reload selected layer(s).

Simple utility to reload/reopen selected layer(s). Reloading updates the data,
reopen also updates the extent. Also provides an option to watch layers
for changes to local file paths and reloads them automatically.
Useful when you're editing the underlying data on the fly in some other program.

In addition to watching layers for changes, joined layers can also be updated 
if the source file is watched. To do this open the `Properties` of the joined 
layer in the `Layers` panel (not the source layer) and select that file's source 
layer in the list under `Dependencies`, then under `Joins` edit the join layer 
and make sure `Cache join layer in memory` is *not* selected. After doing this 
the joined layer should update automatically when the source file changes.

![](screenshot.png)
