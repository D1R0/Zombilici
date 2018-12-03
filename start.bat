@echo off
echo.
pushd %~dp0
%SYSTEMROOT%\py.exe -3 client.py
PAUSE
GOTO end

