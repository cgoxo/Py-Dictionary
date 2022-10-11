import os
import shutil

path = os.getcwd()

arr = os.listdir()

slash = "\\"

# File types and their corresponding extensions
file_types = {
    "Text" : [ ".doc" , ".log" , ".msg" , ".odt" , ".rtf" , ".tex" , ".txt" , ".wpd" , ".wps" , ".docx" , ".pages" ],
    "Data" : [ ".csv" , ".dat", ".ged" , ".key" , ".keychain" , ".pps" , ".ppt" , ".pptx" , ".sdf" , ".tar" , ".tax2016" , ".vcf" , ".xml" ],
    "Audio" : [ ".aif" , ".iff" , ".m3u" , ".m4a" , ".mid" , ".mp3" , ".mpa" , ".wav" , ".wma" ],
    "Video" : [ ".3g2" , ".3gp" , ".asf" , ".avi" , ".flv" , ".m4v" , ".mov" , ".mp4" , ".mpg" , ".rm" , ".srt" ,".swf" , ".vob" , ".wmv" ],
    "3DImage" : [ ".3dm" , ".3ds" , ".max" , ".obj" ],
    "RasterImage" : [ ".bmp" , ".dds" , ".gif" , ".jpg" , ".png" , ".psd" , ".thm" , ".tif" , ".yuv" , ".pspimage" , ".tga" , ".tiff" ],
    "3DImage" : [ ".3dm" , ".3ds" , ".max" , ".obj" ],
    "VectorImage" : [ ".ai" , ".eps" , ".ps" , ".svg" ],
    "PageLayout" : [ ".indd" , ".pct" , ".pdf" ],
    "Spreadsheet" : [ ".xlr" , ".xls" , ".xlsx" ],
    "Database" :  [ ".accdb" , ".db" , ".dbf"  , ".mdb" , ".pdb" , ".sql" ],
    "Executable" : [ ".apk" , ".app" , ".bat" , ".cgi" , ".com" , ".exe" , ".gadget" , ".jar" , ".wsf" ],
    "Game" : [ ".dem" , ".gam" , ".nes" , ".rom" , ".sav" ],
    "CAD" : [ ".dwg" , ".dxf" ],
    "GIS" : [ ".gpx" , ".kml" , ".kmz" ],
    "Web" : [ ".asp" , ".aspx" , ".cer" , ".cfm" , ".csr" , ".css" , ".htm" , ".html" , ".js" , ".jsp" , ".php" , ".rss" , ".xhtml" ],
    "Plugin" : [  ".crx" , ".plugin" ],
    "Font" : [ ".fnt" , ".fon" , ".otf" , ".ttf" ],
    "System" : [ ".cab" , ".cpl" , ".cur" , ".deskthemepack" , ".dll" , ".dmp" , ".drv" , ".icns" , ".ico" , ".lnk" , ".sys" ],
    "Settings" : [ ".cfg" , ".ini" , ".prf" ],
    "Encoded" : [ ".hqx" , ".mim" , ".uue" ],
    "Compressed" : [ ".7z" , ".cbr" , ".deb" , ".gz" , ".pkg" , ".rar" , ".rpm" , ".sitx" , ".tar.gz" , ".zip" , ".zipx" ],
    "DiskImage" : [ ".bin" , ".cue" , ".dmg" , ".iso" , ".mdf" , ".toast" , ".vcd" ],
    "Developer" : [ ".c" , ".class" , ".cpp" , ".cs" , ".dtd" , ".fla" , ".h" , ".java" , ".lua" , ".m" , ".pl" , ".py" , ".sh" , ".sln" , ".swift" , ".vb" , ".vcxproj" , ".xcodeproj" ],
    "Backup" : [ ".bak" , ".tmp" ],
    "Misc" : [ ".crdownload" , ".ics" , ".msi" , ".part" , ".torrent" ]
}

for x in arr:
    fflag=0
    if os.path.isfile(x) and x!="toOrganize.py" and x!="toDisorganize.py":
        if("." in x):
            extension_name = x[x.index("."):]
            for file_type,extensions in file_types.items():
                if extension_name in extensions:
                    fflag=1
                    folder_name = file_type
                    newpath = path + slash + folder_name
                    print(newpath)
                    break

            if (fflag==0):
                folder_name ="Other"
                newpath = path + slash + folder_name
                print(newpath)



        if not os.path.exists(newpath):
            os.makedirs(newpath)

        shutil.move(path + slash + x,newpath + slash +x)
