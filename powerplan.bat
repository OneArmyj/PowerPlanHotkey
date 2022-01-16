@echo off

setlocal

cd /d %~dp0

if "%~1"=="" (
    goto END
)

if /i "%~1" == "extract" (
    goto EXTRACT_GUID
)

@REM Switch powerplan according to GUID chosen
call powercfg /S "%~1"
goto END

:EXTRACT_GUID
    call powercfg /L > powercfg.txt
    goto END

:END
    endlocal
    echo Finishing %~nx0 %~1 
    exit /b 0
    