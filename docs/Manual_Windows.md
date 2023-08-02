# Windows
  
Module for work with Windows configuration  

*Read this in other languages: [English](Manual_Windows.md), [Português](Manual_Windows.pr.md), [Español](Manual_Windows.es.md)*
  
![banner](imgs/Banner_Windows.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Get Screen resolution
  
Return the current resolution of the main screen to a Rocketbot variable
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a variable|Variable where the result will be saved|Variable|

### Get All resolutions
  
Returns all allowed screen resolutions on the main screen
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a variable|Variable where the result will be saved|Variable|

### Change resolution
  
Change the resolution of the main screen to the indicated one. It must be a resolution allowed by the system
|Parameters|Description|example|
| --- | --- | --- |
|Resolution|Screen resolution (width,height)|800,600|

### Get User Name
  
Returns the current user name
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a variable|Variable where the result will be saved|Variable|

### Lock Windows Screen
  
Locks the Windows screen
|Parameters|Description|example|
| --- | --- | --- |

### Is logged in?
  
Checks if the current user is logged in and not on the lockscreen
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a variable|Variable where the result will be saved|Variable|

### Maximize window
  
Maximizes a window by title
|Parameters|Description|example|
| --- | --- | --- |
|Title|Window title to maximize|Window title|

### Restore window
  
Restore a window by title
|Parameters|Description|example|
| --- | --- | --- |
|Title|Window title to restore|Window title|

### Minimize window
  
Minimize a window by title
|Parameters|Description|example|
| --- | --- | --- |
|Title|Window title to minimize|Window title|

### List open windows
  
List open windows by title and handle if you want it
|Parameters|Description|example|
| --- | --- | --- |
|Save in|Variable where the result will be saved|Variable|
|Do you want the handles?|Check if you want the handles of the windows|False|
|Filter|Word to find in the title of the windows|Find word|

### Set foreground window
  
Set window to foreground
|Parameters|Description|example|
| --- | --- | --- |
|Title|Title of the window to set to foreground|Window title|

### Find window
  
Find a window by title
|Parameters|Description|example|
| --- | --- | --- |
|Title|Window title to search|Window title|
|Save in|Variable where the result will be saved|Variable|

### Get service status
  
Get service status
|Parameters|Description|example|
| --- | --- | --- |
|Title||Titulo del servicio|
|Save result in variable|Variable where the result will be saved|Variable|

### Start service
  
Start service
|Parameters|Description|example|
| --- | --- | --- |
|Title|Service title to start|Service title|
|Assign result to variable|Variable where the result will be saved|Variable|

### Stop service
  
Stop service
|Parameters|Description|example|
| --- | --- | --- |
|Title|Service title to stop|Service title|
|Assign result to variable|Variable where the result will be saved|Variable|

### Move and resize window
  
Change position and dimension of windows from title
|Parameters|Description|example|
| --- | --- | --- |
|Title||Title|
|Coordinates (x, y)|Window coordinates on desktop|0,0|
|Dimension (Width, Height)|Window dimensions|0,0|
