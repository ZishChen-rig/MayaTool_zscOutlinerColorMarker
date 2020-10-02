# zscOutlinerColorMarker
![GITHUB](https://1.bp.blogspot.com/-0jIaxfg6eYA/X3cg-gEj0MI/AAAAAAAADfY/Zeg7VfrUdSg_mbE_Mh8TYu29ix0LKK5DQCLcBGAsYHQ/s320/_screenshot.png)
Practice maya tool for mark color on outliner objects

### **Minimum maya version**
2016

### **User Interface**
* Set Color | Hex input button
* Color record area
* Add | Remove | Clear | Save | Load Color record area
* Color record area button operation mode
* Scan outliner color to record
* Mark color to outliner | Remove Marked color

### **Call UI Function**
```py
import zscOutlinerColorMarker.uim
reload(zscOutlinerColorMarker.uim)
zscOutlinerColorMarker.uim.ocm() 
```

### **Note**
This tool just for outliner witch have outlinerColor attribute.

