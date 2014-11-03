@echo off

if "%GCP%" == "" set GCP=..
cd %GCP%/bin
set PYTHONPATH=../


echo =======================================================
echo .
echo .
echo =======================================================
echo .


goto case_%1

:case_start
	cd %GCP%/
	python  lib\gcp\Startup.py
	goto case_end
	
:case_end
	pause