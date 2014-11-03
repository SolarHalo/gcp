@echo off
set a=%1
set env=%a:"=%
set CLASSPATH=%CLASSPATH%;%env%