#include <Windows.h>
#include <iostream>
#include <ctime>
#include <conio.h>

void click(int x, int y) {
    SetCursorPos(x, y);
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);	
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
}

int main() {
    while (!GetAsyncKeyState('Q')) {
        if (GetPixel(GetDC(NULL), 0, 322) == RGB(113, 205, 113)) {
            click(0, 322);
        }
    }
    return 0;
}
