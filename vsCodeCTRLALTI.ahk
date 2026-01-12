#Requires AutoHotkey v2.0
#SingleInstance Force
#UseHook true
SendMode "Input"
SetKeyDelay 30, 30

global startX := 0
global startY := 0
global startT := 0

#HotIf WinActive("ahk_exe Code.exe")

RButton::
{
    global startX, startY, startT
    MouseGetPos &startX, &startY
    startT := A_TickCount
}

RButton Up::
{
    global startX, startY, startT

    ; 左クリック押してたらジェスチャー無効
    if GetKeyState("LButton", "P") {
        Click "Right"
        return
    }

    local endX := 0, endY := 0
    MouseGetPos &endX, &endY

    deltaX := endX - startX
    deltaY := endY - startY
    held  := A_TickCount - startT

    ; まずは大きく動いたら確定
    if (deltaX <= -35 && Abs(deltaY) <= 80) {
        SendInput("{Ctrl up}{Alt up}{Shift up}")
        Sleep 50
        SendInput("^b")
        return
    }
    if (deltaX >= 35 && Abs(deltaY) <= 80) {
        SendInput("{Ctrl up}{Alt up}{Shift up}")
        Sleep 50
        SendInput("^!b")
        return
    }

    ; 長押しなら小さい動きでもジェスチャーにする（メニュー誤発防止）
    if (held >= 150 && Abs(deltaY) <= 100) {
        if (deltaX <= -15) {
            SendInput("{Ctrl up}{Alt up}{Shift up}")
            Sleep 50
            SendInput("^b")
            return
        }
        if (deltaX >= 15) {
            SendInput("{Ctrl up}{Alt up}{Shift up}")
            Sleep 50
            SendInput("^!b")
            return
        }
    }

    ; 普通の右クリック（メニュー）
    Click "Right"
}

#HotIf
