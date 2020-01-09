#include "Rectangle.h"

namespace shapes {
    Rectangle::Rectangle(int x0, int y0, int x1, int y1) {
        this->x0 = x0;
        this->y0 = y0;
        this->x1 = x1;
        this->y1 = y1;
    }

    Rectangle::~Rectangle() {
    }

    int Rectangle::getLength() {
        int l1 = this->x0 - this->x1;
        int l2 = this->y0 - this->y1;
        if (l1 > l2) 
            return l1;
        else 
            return l2;
    }

    int Rectangle::getHeight() {
        int l1 = this->x0 - this->x1;
        int l2 = this->y0 - this->y1;
        if (l1 > l2) 
            return l2;
        else 
            return l1;
    }

    int Rectangle::getArea() {
        int l1 = this->x0 - this->x1;
        int l2 = this->y0 - this->y1;
        return l1 * l2;
    }

    void Rectangle::move(int dx, int dy) {
        this->x0 += dx;
        this->x1 += dx;
        this->y0 += dy;
        this->y1 += dy;
    }
}
