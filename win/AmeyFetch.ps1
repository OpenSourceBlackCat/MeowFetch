$COMPUTER = Get-CimInstance -ClassName Win32_OperatingSystem -ErrorAction Stop;
$CPU_INFO = Get-CimInstance -ClassName Win32_Processor -ErrorAction Stop;
$MOTHERBOARD = Get-CimInstance -ClassName Win32_BaseBoard -ErrorAction Stop;
$GPU_INFO = Get-CimInstance -ClassName Win32_VideoController -ErrorAction Stop;
$Curr_Date = Get-Date;
$SysUPTIME = $Curr_Date - $COMPUTER.LastBootUpTime;
$SHELL = Get-CimInstance -ClassName Win32_Process -Filter "ProcessId=$PID";
$Shell_Info = Get-Process -Id $SHELL[0].ParentProcessId;
$MEM_INFO =  (($COMPUTER.TotalVisibleMemorySize - $COMPUTER.FreePhysicalMemory)/1024)/1024;
$DISK_INFO = (Get-PSDrive -Name C);
$SYS_INFO = @{};
if ($GPU_INFO[1]){
	$GPU_INFO = $GPU_INFO[1];
}
$SYS_INFO[0] = "{0}@{1}" -f $env:USERNAME, (Get-Culture).TextInfo.ToTitleCase($COMPUTER.CSName.ToLower());
$SYS_INFO[1] = "-" * $SYS_INFO[0].Length;
$SYS_INFO[2] = "OS: {0} {1}" -f $COMPUTER.Name.Split("|")[0], $COMPUTER.OSArchitecture;
$SYS_INFO[3] = "HOST: {0}" -f $MOTHERBOARD.Manufacturer;
$SYS_INFO[4] = "KERNEL: {0}" -f $COMPUTER.Version;
$SYS_INFO[5] = "MOTHERBOARD: {0}" -f $MOTHERBOARD.Product;
$SYS_INFO[6] = "UPTIME: {0} Days {1} Hours {2} Minutes" -f $SysUPTIME.Days, $SysUPTIME.Hours, $SysUPTIME.Minutes;
$SYS_INFO[7] = "SHELL: {0}" -f $SHELL.ProcessName;
$SYS_INFO[8] = "RESOLUTION: {0}x{1}" -f  $GPU_INFO.CurrentHorizontalResolution, $GPU_INFO.CurrentVerticalResolution;
$SYS_INFO[9] = "TERMINAL: {0}" -f $Shell_Info.ProcessName;
$SYS_INFO[10] = "CPU: {0}" -f $CPU_INFO.Name;
$SYS_INFO[11] = "GPU: {0}" -f $GPU_INFO.Name;
$SYS_INFO[12] = "MEMORY: {0} GiB / {1} GiB" -f [math]::Round($MEM_INFO, 2), [math]::Round(($COMPUTER.TotalVisibleMemorySize/1024)/1024, 2);
$SYS_INFO[13] = "DISK (C:): {0} GiB / {1} GiB" -f [math]::Round((($DISK_INFO.Used/1024)/1024)/1024, 2), [math]::Round(((($DISK_INFO.Free+$DISK_INFO.Used)/1024)/1024)/1024, 2);
$ASCII_LOGO = "logo.txt";
$ASCII_COLOR = "white-white";
for ($arg=0; $arg -lt $args.Count; $arg++){
    if($args[$arg].ToLower().Contains("--ascii_logo:")){
        $ASCII_LOGO = $args[$arg].ToLower().replace("--ascii_logo:", "");
    }
    if ($args[$arg].ToLower().Contains("--ascii_color:")){
        $ASCII_COLOR = $args[$arg].ToLower().replace("--ascii_color:", "");
    }
}
$LOGO_FILE = Get-Content $ASCII_LOGO;
$LOGO_COLOR = $ASCII_COLOR.split("-")[0];
$TEXT_COLOR = $ASCII_COLOR.split("-")[1];
if ($LOGO_FILE.Count -gt $SYS_INFO.Count){
    for ($i=0; $i -lt $LOGO_FILE.Count; $i++){
        $LOGO_FILE[$i] = $LOGO_FILE[$i].TrimEnd(".");
        try{
            Write-Host $LOGO_FILE[$i] -ForegroundColor $LOGO_COLOR -nonewline; Write-Host $SYS_INFO[$i] -ForegroundColor $TEXT_COLOR;
        }
        catch{
            $SPACE_CHAR = " " * ($LOGO_FILE[0].Length-1);
            Write-Host $LOGO_FILE[$i] -ForegroundColor $SPACE_CHAR -nonewline; Write-Host $SYS_INFO[$i] -ForegroundColor $TEXT_COLOR;
        }
    }
}
else{
    for ($i=0; $i -lt $SYS_INFO.Count; $i++){
        $LOGO_FILE[$i] = $LOGO_FILE[$i].TrimEnd(".");
        try{
            Write-Host $LOGO_FILE[$i] -ForegroundColor $LOGO_COLOR -nonewline; Write-Host $SYS_INFO[$i] -ForegroundColor $TEXT_COLOR;
        }
        catch{
            $SPACE_CHAR = " " * ($LOGO_FILE[0].Length-1);
            Write-Host $LOGO_FILE[$i] -ForegroundColor $SPACE_CHAR -nonewline; Write-Host $SYS_INFO[$i] -ForegroundColor $TEXT_COLOR;
        }
    }
}