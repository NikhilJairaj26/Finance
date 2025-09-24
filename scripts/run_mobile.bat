@echo off

echo =====================================
echo      RUNNING MOBILE APP
echo =====================================

cd ../mobile

:: Start Metro bundler in a new window
start cmd /k "npx react-native start --reset-cache"

:: Run the app on Android
npx react-native run-android
